import streamlit as st
st.title("SachChat")
trang_chu = st.Page("pages/home.py",title="Trang Chủ")
cac_trang = [trang_chu]
menu = st.navigation(cac_trang)
menu.run()
