# lichsu.py
#
# Copyright (C) 2025 Ngô Gia Quý
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License...

import streamlit as st
from thuvien import sach
from thuvien import chat
from thuvien.sach import nap_csdl

cacbaihoc = sach.lay_sach("thuvien/dulieu/lop8/lichsu.txt")
csdl = sach.nap_csdl(cacbaihoc,"thuvien/dulieu/lop8/lichsu.data")


def run():
    st.title("Lịch sử")
    # đoạn lệnh này sẽ hiển thị những thông tin trong phần lịch sử chat
    if "danhsachtinnhan" not in st.session_state:
        st.session_state.danhsachtinnhan = []
    for tin_nhan in st.session_state.danhsachtinnhan:
        st.chat_message(tin_nhan["vaitro"]).markdown(tin_nhan["noidung"])

    cau_hoi = st.chat_input("Hãy nói điều gì đó")

    if cau_hoi:
        st.chat_message("user").markdown(cau_hoi)
        baihoc = sach.lay_bai_hoc(cacbaihoc, csdl, cau_hoi)
        tra_loi = chat.hoi_deepseek(cau_hoi, baihoc)
        st.chat_message("ai").markdown(tra_loi)
        lichsuchat1 = {"vaitro": "user", "noidung": cau_hoi}
        st.session_state.danhsachtinnhan.append(lichsuchat1)
        lichsuchat2 = {"vaitro": "ai", "noidung": tra_loi}
        st.session_state.danhsachtinnhan.append(lichsuchat2)