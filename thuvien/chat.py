# chat.py
#
# Copyright (C) 2025 Ngô Gia Quý
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License...

import requests
import os
from openai import OpenAI

def cau_hoi_day_du(cauhoi, baihoc):
    chdd = "Dựa vào nội dung bài học sau đây, hãy trả lời câu hỏi một cách rõ ràng, mạch lạc và đầy đủ. "\
    + "Nếu câu hỏi không liên quan đến nội dung bài học, hãy trả lời: "\
    "`Xin lỗi, câu hỏi của bạn không liên quan đến nội dung sách.`\n\n"\
    "Nội dung bài học: " + baihoc + "\n\n" \
    "Câu hỏi: " + cauhoi
    return chdd

API_URL = "https://api.deepseek.com/your-endpoint"

HEADERS = {
    "Authorization": f"Bearer {os.getenv("DEEPSEEK_API")}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://sachchat.streamlit.app/",
    "X-Title": "SachChat"
}

def tao_data(cauhoidaydu):
    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "Bạn là trợ lý học tập thông minh và chính xác cho học sinh Việt Nam."},
            {"role": "user", "content": cauhoidaydu}
        ],
    }
    return data

def hoi(cauhoi,baihoc):
    cauhoidaydu = cau_hoi_day_du(cauhoi,baihoc)
    data = tao_data(cauhoidaydu)
    response = requests.post(API_URL,headers=HEADERS,data=data)
    if response.ok:
        traloi = reponse.json()
        noidung = traloi["choices"][0]["message"]["content"]
        return noidung
    else:
        return "Lỗi: " + response.text

def hoi_deepseek(cauhoi,baihoc):
    cauhoidaydu = cau_hoi_day_du(cauhoi,baihoc)
    client = OpenAI(api_key=os.getenv("DEEPSEEK_API"), base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "Bạn là trợ lý học tập thông minh và chính xác cho học sinh Việt Nam."},
            {"role": "user", "content": cauhoidaydu},
        ],
        stream=False
    )
    return response.choices[0].message.content