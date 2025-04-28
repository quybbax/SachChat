# chat.py
#
# Copyright (C) 2025 Ngô Gia Quý
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License...

from langchain_openai import ChatOpenAI
import os
from langchain.chains import RetrievalQA

llm = ChatOpenAI(
    base_url="https://api.deepseek.com/v1",
    api_key=os.getenv("DEEPSEEK_API"),
    model="deepseek-chat",
    temperature=0.7,
    max_tokens=1024
)

def hoi(cauhoi, truyvan):
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=truyvan,
        chain_type="stuff"
        #chain_type="map_reduce"
    )
    traloi = qa.invoke(cauhoi)
    if 'result' in traloi:
        ketqua = traloi['result']
        ketqua = ketqua.replace("các đoạn văn được cung cấp", "sách giáo khoa")
        ketqua = ketqua.replace("thông tin được cung cấp", "sách giáo khoa")
        ketqua = ketqua.replace("tài liệu được cung cấp", "sách giáo khoa")
        return ketqua
    else:
        return "Không tìm thấy câu trả lời trong kết quả."