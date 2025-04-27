# app.py
#
# Copyright (C) 2025 Ngô Gia Quý
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License...

import streamlit as st

# Hiển thị ảnh banner trong sidebar
st.sidebar.image("images/anhtruong.jpg", use_container_width=True)

st.title("SachChat")
trang_chu = st.Page("pages/home.py",title="Trang Chủ")
trang_about = st.Page("pages/about.py",title= "Về Chúng Tôi")
cac_trang = [trang_chu,trang_about]
menu = st.navigation(cac_trang)
menu.run()
