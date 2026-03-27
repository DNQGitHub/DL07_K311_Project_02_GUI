import streamlit as st
import pandas as pd
import numpy as np
import components.sidebar as sidebar
import components.post_card as post_card
import pickle
from sklearn.preprocessing import MinMaxScaler
from helpers.load_data import load_data
from datetime import datetime
from dateutil import relativedelta


# 0   tieu_de              7932 non-null   object
# 1   gia_ban              7932 non-null   object
# 2   don_gia              7932 non-null   object
# 3   dien_tich            7932 non-null   object
# 4   dia_chi              7932 non-null   object
# 5   mo_ta                7932 non-null   object
# 6   dien_thoai           3942 non-null   object
# 7   loai_hinh            7932 non-null   object
# 8   dien_tich_dat        7932 non-null   object
# 9   dien_tich_su_dung    3739 non-null   object
# 10  gia_m2               7932 non-null   object
# 11  giay_to_phap_ly      7932 non-null   object
# 12  so_phong_ngu         7932 non-null   object
# 13  so_phong_ve_sinh     5956 non-null   object
# 14  tong_so_tang         5481 non-null   float64
# 15  tinh_trang_noi_that  7932 non-null   object
# 16  huong_cua_chinh      1315 non-null   object
# 17  dac_diem             7932 non-null   object
# 18  chieu_ngang          6083 non-null   object
# 19  chieu_dai            5947 non-null   object
# 20  ma_can               25 non-null     object
# 21  ten_phan_khu_lo      25 non-null     object
# 22  bieu_do_gia          7932 non-null   object
# 23  source               7932 non-null   object
# 24  gia_ban_num          7932 non-null   float64
# 25  quan                 7932 non-null   object

def display_post_detail(row):
    tieu_de = row['tieu_de']
    gia_ban = row['gia_ban']
    dia_chi = row['dia_chi']
    dien_tich = row['dien_tich']
    mo_ta = row['mo_ta']
    dien_thoai = row['dien_thoai']
    loại_hinh = row['loai_hinh']
    dien_tich_dat = row['dien_tich_dat']
    dien_tich_su_dung = row['dien_tich_su_dung']
    gia_m2 = row['gia_m2']
    giay_to_phap_ly = row['giay_to_phap_ly']
    so_phong_ngu = row['so_phong_ngu']
    so_phong_ve_sinh = row['so_phong_ve_sinh']
    tong_so_tang = row['tong_so_tang']
    tinh_trang_noi_that = row['tinh_trang_noi_that']
    huong_cua_chinh = row['huong_cua_chinh']
    dac_diem = row['dac_diem']
    chieu_ngang = row['chieu_ngang']
    chieu_dai = row['chieu_dai']
    ma_can = row['ma_can']
    ten_phan_khu_lo = row['ten_phan_khu_lo']
    bieu_do_gia = row['bieu_do_gia']

    st.html(f"""
        <div style="display: flex; flex-direction: column; gap: 10px
            ; border: 1px solid #ddd; padding: 20px; border-radius: 5px;">
            <h1 style="margin-top: 0;">{tieu_de}</h1>
            <image src="https://picsum.photos/600/400" alt="Hình ảnh bất động sản" style="width: 100%; border-radius: 5px;">
            <p><strong>Địa chỉ:</strong> {dia_chi}</p>
            <p><strong>Giá bán:</strong> {gia_ban} VND</p>
            <p><strong>Diện tích:</strong> {dien_tich}</p>
            <p><strong>Mô tả:</strong> {mo_ta}</p>
            <p><strong>Điện thoại:</strong> {dien_thoai}</p>
            <p><strong>Loại hình:</strong> {loại_hinh}</p>
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
    
def display_price_chart(bieu_do_gia):
    st.write("### Biểu đồ giá bán theo thời gian")

    if not bieu_do_gia or bieu_do_gia == "[]":
        st.write("Không có dữ liệu biểu đồ giá bán theo thời gian.")
        return
    
    
    gia = bieu_do_gia.replace("[", "").replace("]", "").split(",")
    gia = [float(g.strip()) for g in gia]
    
    time = list(range(1, len(gia) + 1))
    time = [datetime.now() - relativedelta.relativedelta(months=len(gia) - i) for i in range(len(gia))]

    bieu_do_gia_df = pd.DataFrame({
        "price": gia,
        "month": time
    })
        
    st.line_chart(bieu_do_gia_df, x="month", y="price")
    
def display_recommendations(recommendations):
    st.write("### Các bài đăng tương tự")
    
    for index, row in recommendations.iterrows():
        post_card.display(row, index)
        
def load_sim_matrix():
    return pickle.load(open("models/recommendation/sim_matrix_sentence_transformer.pkl", "rb"))

def price_sim(i, j, df):
    return 1 - abs(df.loc[i,"gia_scaled"] - df.loc[j,"gia_scaled"])

def location_sim(i, j, df):
    return 1 if df.loc[i, "quan"] == df.loc[j, "quan"] else 0

def normalize_scores(scores):
    min_s = min(scores)
    max_s = max(scores)

    print(f"Min score: {min_s}, Max score: {max_s}")  # In ra min và max để kiểm tra

    if max_s - min_s == 0:
        return [0]*len(scores)
    
    return [(s - min_s) / (max_s - min_s) for s in scores]

def recommend_house_with_hybrid_sentence_transformer(idx, sim_matrix, df, top_k=5, w_text=0.6, w_price=0.2, w_loc=0.2):
    sims_text = sim_matrix[idx]

    scores = []
    for j in range(len(df)):
        sim_price = price_sim(idx, j, df)
        sim_loc = location_sim(idx, j, df)

        score = (
            w_text * sims_text[j] +
            w_price * sim_price +
            w_loc * sim_loc
        )
        scores.append(score)

    scores = np.array(scores)
    scores_norm = normalize_scores(scores)

    top_idx = np.argsort(scores)[::-1][1:top_k + 1]
    recommended_houses = df.iloc[top_idx]
    recommended_houses['sim_score'] = scores[top_idx]
    recommended_houses['sim_score_norm'] = [scores_norm[i] for i in top_idx]
    return recommended_houses

def main():
    df = load_data()

    scaler = MinMaxScaler()
    df["gia_scaled"] = scaler.fit_transform(df[["gia_ban_num"]])
    
    print("Sample of scaled prices:")
    df.info()
    
    post_id = int(st.query_params.get("post_id", None))
    
    if post_id is not None and 0 <= post_id < len(df):
        row = df.iloc[post_id]

        display_post_detail(row)
        display_price_chart(row['bieu_do_gia'])
        
        sim_matrix = load_sim_matrix()
        recommendations = recommend_house_with_hybrid_sentence_transformer(
            idx=post_id, 
            sim_matrix=sim_matrix, 
            df=df, 
            top_k=5, 
        )
        
        display_recommendations(recommendations)

        st.markdown("---")
        st.markdown("[Quay lại trang danh sách bài đăng](posts)")

    sidebar.display()
    

main()