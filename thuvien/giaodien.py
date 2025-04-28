# giaodien.py
#
# Copyright (C) 2025 Ngô Gia Quý
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License...

import streamlit as st
from . import chat

def giao_dien_chat(title, truyvan):
    st.title(title)
    if "danhsachtinnhan" not in st.session_state:
        st.session_state.danhsachtinnhan = []
    for tin_nhan in st.session_state.danhsachtinnhan:
        st.chat_message(tin_nhan["vaitro"]).markdown(tin_nhan["noidung"])

    cau_hoi = st.chat_input("Hãy nhập câu hỏi của bạn")

    if cau_hoi:
        st.chat_message("user").markdown(cau_hoi)
        tra_loi = chat.hoi(cau_hoi, truyvan)
        st.chat_message("ai").markdown(tra_loi)
        lichsuchat1 = {"vaitro": "user", "noidung": cau_hoi}
        st.session_state.danhsachtinnhan.append(lichsuchat1)
        lichsuchat2 = {"vaitro": "ai", "noidung": tra_loi}
        st.session_state.danhsachtinnhan.append(lichsuchat2)