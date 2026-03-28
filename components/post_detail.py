import streamlit as st

# CSS for post detail styling
_POST_DETAIL_STYLES = """
<style>
    .post-detail-container {
        background: #ffffff;
        border: 1px solid rgba(15, 32, 39, 0.1);
        border-radius: 12px;
        padding: 2rem;
        margin: 1.5rem 0;
    }

    .post-detail-header {
        border-bottom: 2px solid rgba(15, 32, 39, 0.08);
        padding-bottom: 1.5rem;
        margin-bottom: 1.5rem;
    }

    .post-detail-title {
        font-size: 1.7rem;
        font-weight: 800;
        color: #0f2027;
        margin: 0 0 0.8rem 0;
        line-height: 1.3;
    }

    .post-detail-price {
        font-size: 1.5rem;
        font-weight: 800;
        background: linear-gradient(120deg, #0f2027 0%, #203a43 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .post-detail-description {
        font-size: 1rem;
        line-height: 1.7;
        color: #556770;
        margin-bottom: 1.5rem;
    }

    .post-detail-section {
        margin-bottom: 1.5rem;
    }

    .post-detail-section-title {
        font-size: 1rem;
        font-weight: 800;
        color: #142e3a;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid rgba(15, 32, 39, 0.08);
    }

    .post-detail-list {
        display: flex;
        flex-direction: column;
        gap: 0.8rem;
    }

    /* Contact list styling - linear */
    .post-detail-section:nth-of-type(2) .post-detail-list {
        display: flex;
        flex-direction: column;
        gap: 0.8rem;
    }

    .post-detail-section:nth-of-type(2) .post-detail-item {
        display: flex;
        flex-direction: column;
        gap: 0.3rem;
        padding: 0.7rem 0;
        border-bottom: 1px solid rgba(15, 32, 39, 0.05);
    }

    .post-detail-section:nth-of-type(2) .post-detail-item:last-child {
        border-bottom: none;
    }

    /* Info sections styling - grid boxes */
    .post-detail-section:nth-of-type(n+3) .post-detail-list {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
    }

    .post-detail-section:nth-of-type(n+3) .post-detail-item {
        display: flex;
        flex-direction: column;
        gap: 0.3rem;
        padding: 0.8rem;
        background: #ffffff;
        border: 1px solid rgba(15, 32, 39, 0.08);
        border-radius: 6px;
        transition: all 0.3s ease;
    }

    .post-detail-section:nth-of-type(n+3) .post-detail-item:hover {
        border-color: rgba(15, 32, 39, 0.15);
        background: rgba(15, 32, 39, 0.02);
    }

    .post-detail-label {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        font-weight: 700;
        color: #142e3a;
        opacity: 0.6;
    }

    .post-detail-value {
        font-size: 0.9rem;
        color: #203a43;
    }
</style>
"""

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
        {_POST_DETAIL_STYLES}
        <div class="post-detail-container">
            <!-- Header Section -->
            <div class="post-detail-header">
                <div class="post-detail-title">{tieu_de}</div>
                <div class="post-detail-price">💰 {gia_ban} VND</div>
            </div>

            <!-- Description -->
            <div class="post-detail-description">
                {mo_ta}
            </div>

            <!-- Contact Section -->
            <div class="post-detail-section">
                <div class="post-detail-section-title">📞 Thông tin liên hệ</div>
                <div class="post-detail-list">
                    <div class="post-detail-item">
                        <div class="post-detail-label">📍 Địa chỉ</div>
                        <div class="post-detail-value">{dia_chi}</div>
                    </div>
                    <div class="post-detail-item">
                        <div class="post-detail-label">☎️ Điện thoại</div>
                        <div class="post-detail-value">{dien_thoai}</div>
                    </div>
                </div>
            </div>

            <!-- Key Information Section -->
            <div class="post-detail-section">
                <div class="post-detail-section-title">🏠 Thông tin cơ bản</div>
                <div class="post-detail-list">
                    <div class="post-detail-item">
                        <div class="post-detail-label">Loại hình</div>
                        <div class="post-detail-value">{loai_hinh}</div>
                    </div>
                    <div class="post-detail-item">
                        <div class="post-detail-label">Diện tích</div>
                        <div class="post-detail-value">{dien_tich} m²</div>
                    </div>
                    <div class="post-detail-item">
                        <div class="post-detail-label">Giá/m²</div>
                        <div class="post-detail-value">{gia_m2} VND</div>
                    </div>
                    <div class="post-detail-item">
                        <div class="post-detail-label">Phòng ngủ</div>
                        <div class="post-detail-value">{so_phong_ngu}</div>
                    </div>
                    <div class="post-detail-item">
                        <div class="post-detail-label">Phòng vệ sinh</div>
                        <div class="post-detail-value">{so_phong_ve_sinh}</div>
                    </div>
                    <div class="post-detail-item">
                        <div class="post-detail-label">Tổng số tầng</div>
                        <div class="post-detail-value">{tong_so_tang}</div>
                    </div>
                </div>
            </div>

            <!-- Technical Details Section -->
            <div class="post-detail-section">
                <div class="post-detail-section-title">📋 Chi tiết kỹ thuật</div>
                <div class="post-detail-list">
                    <div class="post-detail-item">
                        <div class="post-detail-label">Diện tích đất</div>
                        <div class="post-detail-value">{dien_tich_dat} m²</div>
                    </div>
                    <div class="post-detail-item">
                        <div class="post-detail-label">Diện tích sử dụng</div>
                        <div class="post-detail-value">{dien_tich_su_dung} m²</div>
                    </div>
                    <div class="post-detail-item">
                        <div class="post-detail-label">Chiều ngang</div>
                        <div class="post-detail-value">{chieu_ngang} m</div>
                    </div>
                    <div class="post-detail-item">
                        <div class="post-detail-label">Chiều dài</div>
                        <div class="post-detail-value">{chieu_dai} m</div>
                    </div>
                    <div class="post-detail-item">
                        <div class="post-detail-label">Hướng cửa chính</div>
                        <div class="post-detail-value">{huong_cua_chinh}</div>
                    </div>
                    <div class="post-detail-item">
                        <div class="post-detail-label">Tình trạng nội thất</div>
                        <div class="post-detail-value">{tinh_trang_noi_that}</div>
                    </div>
                </div>
            </div>

            <!-- Additional Information Section -->
            <div class="post-detail-section">
                <div class="post-detail-section-title">✨ Thông tin bổ sung</div>
                <div class="post-detail-list">
                    <div class="post-detail-item">
                        <div class="post-detail-label">Giấy tờ pháp lý</div>
                        <div class="post-detail-value">{giay_to_phap_ly}</div>
                    </div>
                    <div class="post-detail-item">
                        <div class="post-detail-label">Mã căn</div>
                        <div class="post-detail-value">{ma_can}</div>
                    </div>
                    <div class="post-detail-item">
                        <div class="post-detail-label">Phân khu/Lô</div>
                        <div class="post-detail-value">{ten_phan_khu_lo}</div>
                    </div>
                    <div class="post-detail-item">
                        <div class="post-detail-label">Đặc điểm nổi bật</div>
                        <div class="post-detail-value">{dac_diem}</div>
                    </div>
                </div>
            </div>
        </div>
    """)