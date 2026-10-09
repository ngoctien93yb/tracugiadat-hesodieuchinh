import streamlit as st
import pandas as pd
from data import DANH_SACH_DAT

# 1. CẤU HÌNH TRANG WEB
st.set_page_config(page_title="Hệ thống tra cứu giá đất nâng cao", layout="wide")
st.title("🔍 Hệ Thống Tra Cứu Giá Đất & Hệ Số Điều Chỉnh Nâng Cao")
st.write("Tìm kiếm thông tin theo tuyến đường, tính toán tiền sử dụng đất chi tiết.")

# Chuyển dữ liệu gốc sang DataFrame
df = pd.DataFrame(DANH_SACH_DAT)

# 2. KHU VỰC BỘ LỌC TÌM KIẾM
st.subheader("🛠️ Bộ lọc tìm kiếm thông minh")
col1, col2, col3, col4 = st.columns(4)

with col1:
    cac_xa = ["Tất cả"] + list(df["xa"].unique())
    search_xa = st.selectbox("Lọc theo Xã/Phường:", cac_xa)
with col2:
    search_ten = st.text_input("Tìm theo Tên đoạn đường / Từ khóa:", "")
with col3:
    search_ma = st.text_input("Tìm theo Mã đoạn đường:", "")
with col4:
    cac_loai_dat = ["Tất cả"] + list(df["loai_dat"].unique())
    search_loai = st.selectbox("Lọc theo Loại đất gốc:", cac_loai_dat)

# 3. XỬ LÝ LỌC DỮ LIỆU
df_filtered = df.copy()

if search_xa != "Tất cả":
    df_filtered = df_filtered[df_filtered["xa"] == search_xa]
if search_ten:
    df_filtered = df_filtered[df_filtered["ten_duong"].str.contains(search_ten, case=False, na=False)]
if search_ma:
    df_filtered = df_filtered[df_filtered["ma"].str.contains(search_ma, case=False, na=False)]
if search_loai != "Tất cả":
    df_filtered = df_filtered[df_filtered["loai_dat"] == search_loai]

# Chuẩn bị dữ liệu hiển thị lên bảng
df_display = df_filtered.rename(columns={
    "ma": "Mã đoạn",
    "xa": "Xã/Phường",
    "ten_duong": "Tên tuyến đường / Đoạn đường cụ thể",
    "loai_dat": "Loại đất",
    "ktt": "Hệ số thị trường (Ktt)"
})

# 4. HIỂN THỊ BẢNG DỮ LIỆU (Hỗ trợ chọn dòng trực tiếp)
st.markdown("---")
st.subheader(f"📊 Danh sách đoạn đường phù hợp ({len(df_filtered)} kết quả)")
st.info("💡 **Mẹo:** Bạn hãy tích chọn vào ô đầu dòng của một đoạn đường bất kỳ dưới đây để xem biểu mẫu tính toán tiền đất chi tiết.")

# Sử dụng st.dataframe với tính năng selection (chọn dòng)
selected_rows = st.dataframe(
    df_display, 
    use_container_width=True, 
    hide_index=True,
    on_select="rerun",  # Tự động tải lại trang khi bấm chọn dòng
    selection_mode="single"  # Chỉ cho phép chọn 1 dòng tại một thời điểm
)

# 5. BIỂU MẪU TÍNH TIỀN ĐẤT CHI TIẾT KHI DÒNG ĐƯỢC CHỌN
if selected_rows and selected_rows["selection"]["rows"]:
    selected_index = selected_rows["selection"]["rows"]
    
    # Lấy thông tin chi tiết của hàng được chọn
    thong_tin_dat = df_filtered.iloc[selected_index]
    
    st.markdown("---")
    st.header(f"📝 Biểu mẫu tính tiền đất chi tiết: {thong_tin_dat['ma'].values[0]}")
    
    # Tạo 2 cột để bố trí thông tin gốc và thông tin nhập thêm
    col_info, col_calc = st.columns(2)
    
    with col_info:
        st.subheader("📌 Thông tin đoạn đường đã chọn")
        st.markdown(f"**Mã đoạn:** `{thong_tin_dat['ma'].values[0]}`")
        st.markdown(f"**Vị trí:** {thong_tin_dat['ten_duong'].values[0]} (Thuộc {thong_tin_dat['xa'].values[0]})")
        st.markdown(f"**Loại đất gốc:** {thong_tin_dat['loai_dat'].values[0]}")
        st.markdown(f"**Hệ số biến động thị trường (\(K_{{tt}}\)):** `{thong_tin_dat['ktt'].values[0]}` lần")

    with col_calc:
        st.subheader("🧮 Cấu hình thông số thửa đất của bạn")
        
        # Nhập giá đất cơ sở
        giá_đất_bảng = st.number_input(
            "1. Nhập giá đất cơ sở trong Bảng giá đất (VNĐ/m²):", 
            min_value=0, value=1000000, step=100000
        )
        
        # Hệ số Quy hoạch (Kqh - Phụ lục IV)
        DULIEU_KQH = {
            "Đất ở thấp tầng / Đất thương mại dịch vụ (Hệ số sử dụng đất < 4 lần)": 1.00,
            "Đất ở thấp tầng (4 ≤ Hệ số sử dụng đất ≤ 6 lần)": 1.05, 
            "Đất ở thấp tầng (Hệ số sử dụng đất > 6 lần)": 1.15,
            "Các loại đất khác không thuộc nhóm trên": 1.00,
        }
        select_kqh = st.selectbox("2. Chọn Hệ số sử dụng đất quy hoạch (Kqh):", list(DULIEU_KQH.keys()))
        K_qh = DULIEU_KQH[select_kqh]
        
        # Yếu tố ảnh hưởng (Kah - Phụ lục V)
        DULIEU_KAH = {
            "Bình thường / Không có yếu tố ảnh hưởng đặc biệt": 1.00,
            "Thửa đất, khu đất tiếp giáp từ 03 mặt đường trở lên": 1.15,
            "Thửa đất có đường giao thông hướng thẳng vào mặt tiền": 0.95,
            "Thửa đất hướng ra khu nghĩa trang, nghĩa địa, miếu, am, nhà tang lễ": 0.95,
            "Thửa đất hướng ra khu cây xanh, công viên hoặc mặt nước": 1.05,
            "Thửa đất có hệ thống đường dây điện chạy qua bên trên": 0.98,
        }
        select_kah = st.selectbox("3. Chọn Yếu tố ảnh hưởng thửa đất (Kah):", list(DULIEU_KAH.keys()))
        K_ah = DULIEU_KAH[select_kah]
        
        # Nhập diện tích đất để tính tổng tiền
        dien_tich = st.number_input("4. Nhập diện tích thửa đất cần tính toán (m²):", min_value=0.0, value=100.0, step=10.0)

    # 6. TÍNH TOÁN VÀ XUẤT KẾT LUẬN CHI TIẾT
    K_tt = thong_tin_dat['ktt'].values[0]
    K_tong_hop = round(K_tt * K_qh * K_ah, 4)
    gia_dat_cu_the = int(giá_đất_bảng * K_tong_hop)
    tong_tien_dat = int(gia_dat_cu_the * dien_tich)
    
    st.markdown("### 📋 Bảng tổng hợp giá trị thu tiền đất")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Hệ số K Tổng Hợp (\(K = K_{tt} \times K_{qh} \times K_{ah}\))", f"{K_tong_hop} lần")
    m2.metric("Giá đất cụ thể sau điều chỉnh", f"{gia_dat_cu_the:,.0f} VNĐ/m²")
    m3.metric("Tổng tiền sử dụng đất dự kiến", f"{tong_tien_dat:,.0f} VNĐ")
    
    st.success(
        f"📜 **Tóm tắt cách tính toán:**  \n"
        f"Giá đất cụ thể = {giá_đất_bảng:,.0f} VNĐ/m² × ({K_tt} × {K_qh} × {K_ah}) = **{gia_dat_cu_the:,.0f} VNĐ/m²**  \n"
        f"Thành tiền cho {dien_tich} m² = {gia_dat_cu_the:,.0f} VNĐ/m² × {dien_tich} m² = **{tong_tien_dat:,.0f} VNĐ**"
    )
else:
    st.write("ℹ️ *Chưa có đoạn đường nào được chọn để mở biểu mẫu tính toán tiền đất.*")
