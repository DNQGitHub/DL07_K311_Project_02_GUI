import streamlit as st

def display(row, index):
    tieu_de = row['tieu_de']
    gia_ban = row['gia_ban']
    dia_chi = row['dia_chi']
    dien_tich = row['dien_tich']
    so_phong_ngu = row['so_phong_ngu']
    
    st.html(f"""
        <div style="display: flex; flex-direction: column; gap: 10px; border: 1px solid #ddd; padding: 10px; border-radius: 5px; margin-bottom: 10px;">
            <h2 style="margin-top: 10px;">{tieu_de}</h2>
            <div>
                <p>Địa chỉ: {dia_chi}</p>
                <p>Diện tích: {dien_tich}</p>
                <p>Số phòng ngủ: {so_phong_ngu}</p>
                <p>Giá bán: {gia_ban} VND</p>
                <a href="post_detail?post_id={index}" style="color: blue; text-decoration: underline;">Xem chi tiết</a>
            </div>
        </div>
    """)
