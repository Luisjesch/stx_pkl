from pathlib import Path
from langchain.text_splitter import CharacterTextSplitter
import faiss
from langchain.llms import HuggingFaceHub
from langchain.schema import Document
from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
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

lastcnt = 0
allfiles = []
foldersource = input("Folder source name:") or "test"
sourceext = input("Source Docs file extension:") or "md"

ps = list(Path("%s/"%foldersource).glob("**/*.%s"%sourceext))

processed = ""

for ix, p in enumerate(ps):
    loader = TextLoader(p, encoding='utf8')
    documents = loader.load()
    doc = documents[0]
    print(doc.__dict__.keys())
    print('--------------------------FILE %d OUT OF %d --------------------------' % (ix+1,len(ps)))
    tropefilename =str(doc.metadata['source']).split('\\')[-1]
    tropename = tropefilename.replace(" - TV Tropes.md","")
    print('from: %s' % tropefilename)
    print('text: %s' % doc.page_content[0:24])
    strdata = doc.page_content
    tropesections = []

    tropesections = strdata.split("___")
    processed = f"{tropename}: \n" + tropesections[0]
    cte_text = "    open/close all folders "

    for tropesamplelist in tropesections[1:]:
        if cte_text in tropesamplelist:
            tropesamplelist = tropesamplelist.replace(cte_text,"")
        tropesamples = tropesamplelist.split("    ")
        for tropesample in tropesamples:
            if len(tropesample) > 0:
                    tropesample = f"{tropename} Example in " + tropesample
            tropesample = tropesample.replace(" ","")
            tropesample = tropesample.replace("_","**")
            print(tropesample[0:100])
            tropesample = "---\n" + tropesample
            processed += tropesample
    
    with open("tropes/%s.txt"%(tropename), "w",encoding="utf8") as tropefile:
        tropefile.write(processed)
    print("%s processed!" % tropename)

