from pathlib import Path
from langchain.text_splitter import CharacterTextSplitter
import faiss
from langchain.llms import HuggingFaceHub
from langchain.schema import Document
from langchain.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
import chromadb
import re
import os
import random
import json
import time
import uuid
from datetime import datetime
import bson

os.environ["OPENAI_API_KEY"] ="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"
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
# List all markdown documents in the provided directory.

print("Loading Text Files...")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
fulldb = None

lastcnt = 0
allfiles = []

ingestdir = input('Dir name to ingest:')
ps = list(Path("%s/"%ingestdir).glob("**/*.txt"))


if os.path.isfile("processed_%s.txt"%ingestdir):
    with open("processed_%s.txt"%ingestdir, "r") as pd:
        allfiles = pd.read()
        allfiles = allfiles.split("\n")

# if os.path.isfile("vdbs/testchroma.bs"):
#     index = faiss.read_index("testchroma.index")
#     with open("vdbs/testchroma.bs", "rb") as f:
#         bdata = f.read()
#         sdata = bson.loads(bdata)
#         fulldb = sdata['data']
#     fulldb.index = index

docstoindex = []
processedtropes = []

persistent_client = chromadb.PersistentClient(path="vdbs/%s_db"%ingestdir)
collection = persistent_client.get_or_create_collection(ingestdir)
db = Chroma(client=persistent_client,collection_name=ingestdir,embedding_function=embeddings)

for ix, p in enumerate(ps):
    try:
        print(f"{p.name}")
        pname = f"{p.name}"
        if p.name in allfiles:
            print('%s already processed! Skipping!' % pname)
            continue
        print('1--------------------------------')
        loader = TextLoader(p, encoding='utf8')
        documents = loader.load()
        doc = documents[0]
        strdata = doc.page_content
        doc_content = str(doc.page_content).split('---')
        doc_metadata = dict(doc.metadata)
        pars = []
        lines = ""
        print('2--------------------------------')

        for line in doc_content:
            if len(line) < 100:
                continue
            pars.append(line)

        for ipar,par in enumerate(list(pars)):
            if len(par)==0:
                continue
            dtnow = datetime.now()
            srcpath = "%s/%s.txt" % (ingestdir,pname)
            doc_metadata.update({'lastupdate': dtnow,'src':srcpath})
            for mtdt in doc_metadata:
                doc_metadata[mtdt]=str(doc_metadata[mtdt])
            doctoindex = Document(page_content=str(par), metadata=doc_metadata)
            docstoindex.append(doctoindex)
            collection.add(
                ids=[str(uuid.uuid1())], metadatas=doc_metadata, documents=par
            )
            print(f"3{ipar}--------------------------------")

    
    except Exception as e:
        print(e)
        print("%s skipped!"%p)
        continue

# dbtest
qry="'90s Anti-Hero Example in Comic Strips"
docs = db.similarity_search(qry)
print(docs)
# embeddings = OpenAIEmbeddings(open_api_key="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",model="ada",max_retries=3, request_timeout=60)
# embeddings = LlamaCppEmbeddings(model_path="/models/ggml-alpaca-7b-q4.bin",n_gpu_layers=4)
