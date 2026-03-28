import streamlit as st

def display(post):
    tieu_de = post['tieu_de']
    gia_ban = post['gia_ban']
    dia_chi = post['dia_chi']
    dien_tich = post['dien_tich']
    mo_ta = post['mo_ta']
    dien_thoai = post['dien_thoai']
    loai_hinh = post['loai_hinh']
    dien_tich_dat = post['dien_tich_dat']
    dien_tich_su_dung = post['dien_tich_su_dung']
    gia_m2 = post['gia_m2']
    giay_to_phap_ly = post['giay_to_phap_ly']
    so_phong_ngu = post['so_phong_ngu']
    so_phong_ve_sinh = post['so_phong_ve_sinh']
    tong_so_tang = post['tong_so_tang']
    tinh_trang_noi_that = post['tinh_trang_noi_that']
    huong_cua_chinh = post['huong_cua_chinh']
    dac_diem = post['dac_diem']
    chieu_ngang = post['chieu_ngang']
    chieu_dai = post['chieu_dai']
    ma_can = post['ma_can']
    ten_phan_khu_lo = post['ten_phan_khu_lo']

    st.html(f"""
        <div style="display: flex; flex-direction: column; gap: 10px
            ; border: 1px solid #ddd; padding: 20px; border-radius: 5px;">
            <h1 style="margin-top: 0;">{tieu_de}</h1>
            <p><strong>Địa chỉ:</strong> {dia_chi}</p>
            <p><strong>Giá bán:</strong> {gia_ban} VND</p>
            <p><strong>Diện tích:</strong> {dien_tich}</p>
            <p><strong>Mô tả:</strong> {mo_ta}</p>
            <p><strong>Điện thoại:</strong> {dien_thoai}</p>
            <p><strong>Loại hình:</strong> {loai_hinh}</p>
            <p><strong>Diện tích đất:</strong> {dien_tich_dat}</p>
            <p><strong>Diện tích sử dụng:</strong> {dien_tich_su_dung}</p>
            <p><strong>Giá/m2:</strong> {gia_m2} VND</p>
            <p><strong>Giấy tờ pháp lý:</strong> {giay_to_phap_ly}</p>
            <p><strong>Số phòng ngủ:</strong> {so_phong_ngu}</p>
            <p><strong>Số phòng vệ sinh:</strong> {so_phong_ve_sinh}</p>
            <p><strong>Tổng số tầng:</strong> {tong_so_tang}</p>
            <p><strong>Tình trạng nội thất:</strong> {tinh_trang_noi_that}</p>
            <p><strong>Hướng cửa chính:</strong> {huong_cua_chinh}</p>
            <p><strong>Đặc điểm nổi bật:</strong> {dac_diem}</p>
            <p><strong>Chiều ngang:</strong> {chieu_ngang} m</p>
            <p><strong>Chiều dài:</strong> {chieu_dai} m</p>
            <p><strong>Mã căn:</strong> {ma_can}</p>
            <p><strong>Tên phân khu lô:</strong> {ten_phan_khu_lo}</p>
        </div>
    """)