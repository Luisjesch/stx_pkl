from pathlib import Path
from langchain.text_splitter import CharacterTextSplitter
import faiss
from langchain.llms import HuggingFaceHub
from langchain.schema import Document
from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
import re
import os
import random
import json
import time
from datetime import datetime
try:
   import cPickle as pickle
except:
   import pickle

os.environ["OPENAI_API_KEY"] ="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"
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
# List all markdown documents in the provided directory.


print("Loading Text Files...")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
fulldb = None

lastcnt = 0
allfiles = []
ps = list(Path("tropes/").glob("**/*.txt"))

# mood, emotion, theme, situation
if os.path.isfile("processed_tropes.txt"):
    with open("processed_tropes.txt", "r") as pd:
        allfiles = pd.read()
        allfiles = allfiles.split("\n")


if os.path.isfile("vdbs/tropes.pkl"):
    index = faiss.read_index("tropes.index")
    with open("vdbs/tropes.pkl", "rb") as f:
        fulldb = pickle.load(f)    
    fulldb.index = index


if fulldb is None:
    fulldb = store
else:
    fulldb.merge_from(store)

docstoindex = []
processedtropes = []

for ix, p in enumerate(ps):
    try:
        print(f"{p.name}")
        if p.name in allfiles:
            print('%s already processed! Skipping!' % p.name)
            continue
        loader = TextLoader(p, encoding='utf8')
        documents = loader.load()
        doc = documents[0]
        strdata = doc.page_content
        doc_content = str(doc.page_content).split('---')
        doc_metadata = dict(doc.metadata)
        pars = []
        lines = ""
        for line in doc_content:
            if len(line) < 100:
                continue
            pars.append(line)

        sumindex={}

        for ipar,par in enumerate(list(pars)):
            if len(par)==0:
                continue

            dtnow = datetime.now()
            srcpath = "tropes/%s.txt" % p.name
            doc_metadata.update({'lastupdate': dtnow,'src':srcpath})
            doctoindex = Document(page_content=str(par), metadata=dict(doc_metadata))
            docstoindex.append(doctoindex)

        processedtropes.append(p.name)
    
    except Exception as e:
        print(e)
        print("%s skipped!"%p)

store = FAISS.from_documents(docstoindex, embeddings)

faiss.write_index(fulldb.index, "docs.index")

with open("vdbs/tropes.pkl", "wb") as f:
    pickle.dump(fulldb, f)

with open("processed_tropes.txt", "a+") as pd:
    allprocessed = "\n".join(processedtropes)
    pd.write("%s\n"%p.name)
    
print("%s processed!" % p)
# embeddings = OpenAIEmbeddings(open_api_key="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",model="ada",max_retries=3, request_timeout=60)
# embeddings = LlamaCppEmbeddings(model_path="/models/ggml-alpaca-7b-q4.bin",n_gpu_layers=4)
