# gddp.py
#
# Copyright (C) 2025 Ngô Gia Quý
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License...

import streamlit as st
from thuvien import sach
from thuvien import chat
from thuvien import giaodien

cacbaihoc = sach.lay_sach("thuvien/dulieu/lop8/gddp.txt")
csdl = sach.nap_csdl(cacbaihoc,"thuvien/dulieu/lop8/gddp.data")


def run():
    giaodien.giao_dien_chat("Giáo dục địa phương", cacbaihoc, csdl)
