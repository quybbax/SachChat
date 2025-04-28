# gddp.py
#
# Copyright (C) 2025 Ngô Gia Quý
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License...

from thuvien import sach
from thuvien import giaodien

csdl = sach.nap_csdl("thuvien/dulieu/lop8/gdcd.in","thuvien/dulieu/lop8/gdcd8-kntt")
truyvan = csdl.as_retriever()

def run():
    giaodien.giao_dien_chat("Giáo dục công dân", truyvan)
