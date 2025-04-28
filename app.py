# app.py
#
# Copyright (C) 2025 Ngô Gia Quý
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License...

import streamlit as st
import importlib

st.set_page_config(
    page_title="SachChat - Sản phầm dự thi Sáng tạo TTN-NĐ Quảng Ngãi lần 10 - 2025",
)

# Hiển thị ảnh banner trong sidebar
st.sidebar.image("images/anhtruong.jpg", use_container_width=True)
st.sidebar.title("SachChat")

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
        ["---", "Giáo dục công dân", "Giáo dục địa phương", "Lịch sử"]
    )
    subject_files = {
        "Giáo dục công dân": "gdcd",
        "Giáo dục địa phương": "gddp",
        "Lịch sử": "lichsu"
    }
    selected_file = subject_files.get(subject)

    if selected_file:
        # Import và chạy module tương ứng
        module = importlib.import_module(selected_file)
        module.run()
    else:
        st.write("# Hãy chọn môn học")

st.sidebar.markdown("<hr>", unsafe_allow_html=True)
st.sidebar.markdown("""Nhóm dự thi lớp 8A Trường THCS Nguyễn Nghiêm, Đức Phổ. 
Thành viên: 
* Ngô Gia Quý
* Huỳnh Nguyễn Thảo Vi
* Võ Huỳnh Như Quỳnh
* Phạm Quang Minh""")