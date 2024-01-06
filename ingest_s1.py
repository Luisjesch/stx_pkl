from pathlib import Path
from langchain.text_splitter import CharacterTextSplitter
import faiss
from langchain.llms import HuggingFaceHub
from langchain.schema import Document
from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.embeddings import OpenAIEmbeddings
from langchain.embeddings import LlamaCppEmbeddings
from hugchat import hugchat
from hugchat.login import Login
from langchain.text_splitter import RecursiveCharacterTextSplitter
import re
import os
import nltk
import asyncio
import random
import json
import time
import hashlib
try:
   import cPickle as pickle
except:
   import pickle

os.environ["OPENAI_API_KEY"] ="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"
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
# List all markdown documents in the provided directory.


sign = Login("ex3y7jr0r@mozmail.com", '8HP_S,m)@U"z^&S')
cookies = sign.login()
cookie_path_dir = "./cookies_snapshot"
sign.saveCookiesToDir(cookie_path_dir)

print("Loading Text Files...")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
fulldb = None

lastcnt = 0
allfiles = []
picklefilename = input("Pickle file name:") or "data_s1"
foldersource = input("Folder source name:") or "tests"
sourceext = input("Source Docs file extension:") or "md"
processorlistfname = input("Processor file name:") or "processeddatas1"
indexfoldername = input("Summary index folder name:") or "tests"

ps = list(Path("%s/"%foldersource).glob("**/*.%s"%sourceext))

if os.path.isfile("%s/%s.txt"%(foldersource,processorlistfname)):
    with open("%s/%s.txt"%(foldersource,processorlistfname), "r") as pd:
        allfiles = pd.readlines()

    for i, fname in enumerate(ps):
        if fname in allfiles:
            del ps[i]

processed = []

if os.path.isfile("vdbs/%s.pkl"%picklefilename):
    with open("vdbs/%s.pkl"%picklefilename, "rb") as f:
        fulldb = pickle.load(f)

chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"
id = chatbot.new_conversation()
chatbot.change_conversation(id)
chatbot.switch_llm(4)

# mood, emotion, theme, situation
async def summarizetext(query):
    instructions="Create a comprehensive summary of the scenes, sections or parts of the text referenced here, and provide explanation if possible."
    instructions+="Use the following text as reference: %s" % query
    print("query> %s" % instructions[0:24])
    chatbotresponse = chatbot.query(instructions, web_search=False)
    return chatbotresponse

for ix, p in enumerate(ps):
    try:
        loader = TextLoader(p, encoding='utf8')
        documents = loader.load()
        doc = documents[0]
        print(doc.metadata)
        print('--------------------------FILE %d OUT OF %d --------------------------' % (ix+1,len(ps)))
        print('from: %s' % doc.metadata['source'])
        print('text: %s' % doc.page_content[0:24])
        strdata = doc.page_content
        strdata = strdata.replace(" ","")
        doc_content = nltk.sent_tokenize(doc.page_content)
        doc_metadata = dict(doc.metadata)
        pars = []
        lines = ""
        for line in doc_content:
            lines += line
            if len(lines) > 500:
                pars.append(lines)
                lines=""
                print('---------> added: %s' % line[0:64].replace('\n',''))
        pars.append(lines)
        print('---------> added last: %s' % line[0:64].replace('\n',''))
        print("!! %d embeddings to make."%len(pars))
        docstoindex = []
        sumindex={}

        sumindexfile = "%s/%s_index.json"%(indexfoldername,p.name)
        for ipar,par in enumerate(list(pars)):
            if len(par)==0:
                continue
            print('PAR. %d/%d : %s' % (ipar,len(pars),p.name))

            f32c = "%s-%d-%d" % (p.name,ix,ipar)
            vecthash = hashlib.md5(str(f32c).encode('utf-8')).hexdigest()
            print('??? q: %s' % vecthash)
            
            # par_summary = asyncio.run(summarizetext(str(par)))
            # print("HFC >>> %s" % par_summary[0:24])

            # with open("indexed_data/%s.txt" % p.name, "a+") as pd:
            #     pd.write(par_summary+"\n---\n")

            sumindex.update({vecthash: "You can edit this to add notes for this text."})
            doc_metadata.update({'hashid': vecthash,'sumindex': sumindexfile})
            doctoindex = Document(page_content=str(par), metadata=dict(doc_metadata))
            docstoindex.append(doctoindex)

        with open(sumindexfile, 'w') as rwf:
            rwf.write(json.dumps(sumindex))
        
        store = FAISS.from_documents(docstoindex, embeddings)
        if fulldb is None:
            fulldb = store
        else:
            fulldb.merge_from(store)

        print("%s embedded!" % p)
        processed.extend(p.name)

        faiss.write_index(fulldb.index, "docs.index")

        with open("vdbs/%s.pkl" % picklefilename, "wb") as f:
            pickle.dump(fulldb, f)

        with open("%s/%s.txt"%(foldersource,processorlistfname), "a+") as pd:
            pd.write("%s \n"%p.name)
        print("%s processed!" % p)

    except Exception as e:
        print(e)
        print("%s skipped!"%p)


# embeddings = OpenAIEmbeddings(open_api_key="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",model="ada",max_retries=3, request_timeout=60)
# embeddings = LlamaCppEmbeddings(model_path="/models/ggml-alpaca-7b-q4.bin",n_gpu_layers=4)
