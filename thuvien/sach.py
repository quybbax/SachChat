# sach.py
#
# Copyright (C) 2025 Ngô Gia Quý
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License...

import faiss
import os
from sentence_transformers import SentenceTransformer
from . import descript

from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.vectorstores import FAISS

def lay_sach(ten_file):
    f=open(ten_file,"rb")
    noidung = f.read()
    noidung = descript.decrypt(noidung, os.getenv("CRYPTO_CODE"))
    tailieu = [Document(page_content=noidung)]
    tachroi = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    sach = tachroi.split_documents(tailieu)
    return sach

mohinh = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

def ghi_csdl(sach, file_csdl):
    csdl = FAISS.from_documents(sach, mohinh)
    csdl.save_local(file_csdl)

def doc_csdl(file_csdl):
    csdl = FAISS.load_local(file_csdl, mohinh, allow_dangerous_deserialization=True)
    return csdl

def nap_csdl(file_sach, file_csdl):
    sach = lay_sach(file_sach)
    if not os.path.exists(file_csdl):
        ghi_csdl(sach, file_csdl)
    csdl = doc_csdl(file_csdl)
    return csdl
