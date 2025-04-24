import faiss
import os
from sentence_transformers import SentenceTransformer
def lay_sach(ten_file):
    f=open(ten_file,"r",encoding="utf-8")
    noidung = f.read()
    dsbaihoc = noidung.split("\n\n")
    return (dsbaihoc)

mohinh = SentenceTransformer ("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
def ghi_csdl(danhsachbaihoc, file_csdl):
    vector = mohinh.encode(danhsachbaihoc)
    kichthuoc = mohinh.get_sentence_embedding_dimension()
    csdl = faiss.IndexFlatL2(kichthuoc)
    csdl.add(vector)
    faiss.write_index(csdl, file_csdl)

def doc_csdl(file_csdl):
    csdl = faiss.read_index(file_csdl)
    return csdl

def nap_csdl(dsbaihoc, file_csdl):
    if not os.path.exists(file_csdl):
        ghi_csdl(dsbaihoc, file_csdl)
    csdl = doc_csdl(file_csdl)
    return csdl

def lay_bai_hoc(dsbaihoc,csdl,cauhoi):
    vector = mohinh.encode([cauhoi])
    D, I = csdl.search(vector, k=1)
    baihoc = dsbaihoc[I[0][0]]
    return baihoc