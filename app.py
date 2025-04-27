# app.py
#
# Copyright (C) 2025 Ngô Gia Quý
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License...

import streamlit as st
import importlib

# Hiển thị ảnh banner trong sidebar
st.sidebar.image("images/anhtruong.jpg", use_container_width=True)
st.sidebar.title("SachChat")
#trang_chu = st.Page("thuvien/home.py",title="Trang Chủ")
#trang_about = st.Page("thuvien/about.py",title= "Về Chúng Tôi")
#cac_trang = [trang_chu,trang_about]
#menu = st.navigation(cac_trang)
#menu.run()
selected_class = st.sidebar.selectbox(
    "Chọn lớp:",
    [
        "---",
        "Lớp 8 (Bộ sách KNTT)"
    ]
)
if selected_class == "Lớp 8 (Bộ sách KNTT)":
    st.sidebar.title("Chọn môn học")
    subject = st.sidebar.selectbox(
        "Môn học:",
        ["Lịch sử", "Địa lý", "Giáo dục công dân", "Giáo dục địa phương"]
    )
    subject_files = {
        "Lịch sử": "lichsu",
        "Địa lý": "dialy",
        "Giáo dục công dân": "giaoduccongdan",
        "Giáo dục địa phương": "gddp"
    }
    selected_file = subject_files.get(subject)

    if selected_file:
        # Import và chạy module tương ứng
        module = importlib.import_module(selected_file)
        module.run()  # Giả sử trong mỗi file có hàm `run()`
    else:
        st.write("Chưa có nội dung cho môn học này.")

st.sidebar.markdown("<hr>", unsafe_allow_html=True)
st.sidebar.markdown("""Nhóm dự thi lớp 8A Trường THCS Nguyễn Nghiêm, Đức Phổ. 
Thành viên: 
* Ngô Gia Quý
* Huỳnh Nguyễn Thảo Vi
* Võ Huỳnh Như Quỳnh
* Phạm Quang Minh""")