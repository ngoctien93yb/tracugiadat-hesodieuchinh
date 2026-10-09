# data.py
# Danh mục Hệ số điều chỉnh mức biến động thị trường (Ktt) - Lào Cai 2026

DANH_SACH_DAT = [
    # ĐẤT NÔNG NGHIỆP
    {"ma": "NN-01", "xa": "Sa Pa", "ten_duong": "Đất trồng lúa, cây hàng năm, lâu năm, rừng, thủy sản...", "loai_dat": "Đất nông nghiệp", "ktt": 1.2},
    {"ma": "NN-02", "xa": "Sa Pa", "ten_duong": "Đất nông nghiệp cùng thửa có nhà ở, tiếp giáp đất ở", "loai_dat": "Đất nông nghiệp", "ktt": 1.2},
    {"ma": "NN-03", "xa": "Các xã còn lại", "ten_duong": "Đất trồng lúa, cây hàng năm, lâu năm, rừng...", "loai_dat": "Đất nông nghiệp", "ktt": 1.0},
    {"ma": "NN-04", "xa": "Các xã còn lại", "ten_duong": "Đất nông nghiệp cùng thửa hoặc tiếp giáp đất ở", "loai_dat": "Đất nông nghiệp", "ktt": 1.0},
    
    # XÃ BẢO ÁI
    {"ma": "BA-01", "xa": "Bảo Ái", "ten_duong": "Quốc lộ 70: Từ ranh giới xã Yên Bình đến cống qua đường (đối diện nhà ông Hải)", "loai_dat": "Đất ở / Phi nông nghiệp", "ktt": 1.11},
    {"ma": "BA-02", "xa": "Bảo Ái", "ten_duong": "Quốc lộ 70: Đoạn tiếp theo đến ngã ba đường Cảm Ân đi Tân Đồng", "loai_dat": "Đất ở / Phi nông nghiệp", "ktt": 1.11},
    {"ma": "BA-03", "xa": "Bảo Ái", "ten_duong": "Quốc lộ 70: Đoạn tiếp theo đến cống qua đường (đối diện nhà ông Ngọ)", "loai_dat": "Đất ở / Phi nông nghiệp", "ktt": 1.30},
    {"ma": "BA-04", "xa": "Bảo Ái", "ten_duong": "Quốc lộ 70: Đoạn tiếp theo đến cống qua đường (đối diện nhà bà Nguyễn Thị Cúc)", "loai_dat": "Đất ở / Phi nông nghiệp", "ktt": 1.30},
    {"ma": "BA-05", "xa": "Bảo Ái", "ten_duong": "Quốc lộ 70: Đoạn tiếp theo đến hết ranh giới đất nhà nghỉ Trung Kiên", "loai_dat": "Đất ở / Phi nông nghiệp", "ktt": 1.20},
    {"ma": "BA-26", "xa": "Bảo Ái", "ten_duong": "Các tuyến đường khác còn lại tại xã Bảo Ái", "loai_dat": "Đất ở / Phi nông nghiệp", "ktt": 2.50},

    # XÃ CẢM NHÂN
    {"ma": "CN-01", "xa": "Cảm Nhân", "ten_duong": "Đường Vĩnh Kiên - Yên Thế: Đoạn từ giáp xã Yên Thành đến Cầu Sắt", "loai_dat": "Đất ở / Phi nông nghiệp", "ktt": 1.00},
    {"ma": "CN-06", "xa": "Cảm Nhân", "ten_duong": "Đường Vĩnh Kiên - Yên Thế: Đoạn tiếp theo đến giáp xã Yên Thành", "loai_dat": "Đất ở / Phi nông nghiệp", "ktt": 1.60},
    {"ma": "CN-17", "xa": "Cảm Nhân", "ten_duong": "Đường từ ngã ba chân đèo Tắng Sính đến đỉnh đèo Tắng Sính (Thôn Ngọc Chấn 1)", "loai_dat": "Đất ở / Phi nông nghiệp", "ktt": 1.50},
    {"ma": "CN-32", "xa": "Cảm Nhân", "ten_duong": "Các tuyến đường khác còn lại tại xã Cảm Nhân", "loai_dat": "Đất ở / Phi nông nghiệp", "ktt": 1.10},

    # XÃ THÁC BÀ
    {"ma": "TB-01", "xa": "Thác Bà", "ten_duong": "Quốc lộ 37: Đoạn giáp ranh tỉnh Phú Thọ đến nhà bà Tâm Thắng", "loai_dat": "Đất ở / Phi nông nghiệp", "ktt": 1.10},
    {"ma": "TB-03", "xa": "Thác Bà", "ten_duong": "Quốc lộ 37: Đoạn tiếp theo đến ngã ba đường bê tông (rẽ vào thôn Đại Thân)", "loai_dat": "Đất ở / Phi nông nghiệp", "ktt": 1.70},
    {"ma": "TB-04", "xa": "Thác Bà", "ten_duong": "Quốc lộ 37: Đoạn tiếp theo đến hết thôn Làng Cần", "loai_dat": "Đất ở / Phi nông nghiệp", "ktt": 1.50},
    {"ma": "TB-32", "xa": "Thác Bà", "ten_duong": "Các tuyến đường khác còn lại tại xã Thác Bà", "loai_dat": "Đất ở / Phi nông nghiệp", "ktt": 1.50},

    # XÃ YÊN BÌNH
    {"ma": "YB-01", "xa": "Yên Bình", "ten_duong": "Quốc lộ 70: Từ đường Đại Đồng đến mốc Km1 thôn Làng Đát", "loai_dat": "Đất ở / Phi nông nghiệp", "ktt": 1.00},
    {"ma": "YB-12", "xa": "Yên Bình", "ten_duong": "Đường Tân Quang: Từ sau vị trí 1 đường Đại Đồng đến hết đất Trường Nội trú", "loai_dat": "Đất ở / Phi nông nghiệp", "ktt": 1.80},
    {"ma": "YB-40", "xa": "Yên Bình", "ten_duong": "Các tuyến đường khác còn lại tại xã Yên Bình", "loai_dat": "Đất ở / Phi nông nghiệp", "ktt": 1.50},

    # XÃ YÊN THÀNH
    {"ma": "YT-01", "xa": "Yên Thành", "ten_duong": "Tỉnh Lộ 170: Đoạn từ giáp xã Thác Bà đến nhà ông Bình Tuyến", "loai_dat": "Đất ở / Phi nông nghiệp", "ktt": 1.50},
    {"ma": "YT-24", "xa": "Yên Thành", "ten_duong": "Đường tránh đi cầu treo: Đoạn tiếp theo đến đường Tỉnh lộ 170", "loai_dat": "Đất ở / Phi nông nghiệp", "ktt": 1.55},
    {"ma": "YT-25", "xa": "Yên Thành", "ten_duong": "Các tuyến đường khác còn lại tại xã Yên Thành", "loai_dat": "Đất ở / Phi nông nghiệp", "ktt": 1.80},
]
