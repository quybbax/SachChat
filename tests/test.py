#import tienich
#tienich.lay_sach("dulieu/lop8/lichsu.txt")

#from tienich import lay_sach
#a=lay_sach("dulieu/lop8/lichsu.txt")



"""
cacbaihoc = tienich.lay_sach("dulieu/lop8/lichsu.txt")
#cauhoi = "Vào đầu thế kỉ XVII, nước nào có nền kinh tế phát triển nhất châu Âu"
cauhoi = "E. Các-rai phát minh ra máy dệt, đưa tốc độ sản xuất tăng lên 39 lần vào năm nào"
csdl = tienich.nap_csdl(cacbaihoc,"lichsu1.data")
baihoc = tienich.lay_bai_hoc(cacbaihoc, csdl, cauhoi)
print(baihoc)
"""


from pages.chat import cau_hoi_day_du

bailam = cau_hoi_day_du("python là gì?","python ngôn ngữ lập trình bậc cao")
print(bailam)

