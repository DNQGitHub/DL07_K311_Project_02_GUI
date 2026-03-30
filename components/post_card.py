import streamlit as st

# CSS for post card styling
_POST_CARD_STYLES = """
<style>
    .post-card {
        background: #ffffff;
        border: 1px solid rgba(15, 32, 39, 0.1);
        border-radius: 10px;
        padding: 1.25rem;
        margin-bottom: 1rem;
        box-shadow: none;
        transition: all 0.3s ease;
    }

    .post-card:hover {
        border-color: rgba(15, 32, 39, 0.2);
        background: rgba(15, 32, 39, 0.02);
    }

    .post-card-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #0f2027;
        margin: 0 0 0.8rem 0;
        line-height: 1.35;
        word-break: break-word;
    }

    .post-card-info {
        display: flex;
        gap: 2rem;
        margin-bottom: 0.8rem;
        font-size: 0.95rem;
    }

    .post-card-item {
        display: flex;
        flex-direction: column;
        gap: 0.3rem;
    }

    .post-card-label {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        font-weight: 600;
        color: #142e3a;
        opacity: 0.6;
    }

    .post-card-value {
        font-size: 0.95rem;
        font-weight: 600;
        color: #203a43;
    }

    .post-card-address {
        font-size: 0.9rem;
        color: #556770;
        margin-bottom: 1rem;
    }

    .post-card-price {
        font-size: 1.1rem;
        font-weight: 700;
        color: #0f2027;
        margin-bottom: 1rem;
    }

    .post-card-action {
        display: flex;
        gap: 0.8rem;
    }

    .post-card-link {
        display: inline-block;
        padding: 0.7rem 1.2rem;
        background: linear-gradient(135deg, #ff6b35 0%, #ff4757 100%);
        color: #ffffff;
        text-decoration: none;
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.9rem;
        text-align: center;
        transition: all 0.3s ease;
        border: none;
    }

    .post-card-link:hover {
        background: linear-gradient(135deg, #ff7f50 0%, #ff6b6b 100%);
    }
</style>
"""

def display(row, index):
    tieu_de = row['tieu_de']
    gia_ban = row['gia_ban']
    dia_chi = row['dia_chi']
    dien_tich = row['dien_tich']
    so_phong_ngu = row['so_phong_ngu']
    
    st.html(f"""
        {_POST_CARD_STYLES}
        <div class="post-card">
            <div class="post-card-title">{tieu_de}</div>
            
            <div class="post-card-address">📍 {dia_chi}</div>
            
            <div class="post-card-info">
                <div class="post-card-item">
                    <div class="post-card-label">Diện tích</div>
                    <div class="post-card-value">{dien_tich}</div>
                </div>
                <div class="post-card-item">
                    <div class="post-card-label">Phòng ngủ</div>
                    <div class="post-card-value">{so_phong_ngu} phòng</div>
                </div>
            </div>
            
            <div style="margin-bottom: 1rem;">
                <div class="post-card-label">Giá bán</div>
                <div class="post-card-price">💰 {gia_ban} VND</div>
            </div>
            
            <div class="post-card-action">
                <a href="post_detail?post_id={index}" class="post-card-link">Xem chi tiết →</a>
            </div>
        </div>
    """)

