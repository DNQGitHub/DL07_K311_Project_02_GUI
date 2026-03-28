import streamlit as st
import pandas as pd
import components.sidebar as sidebar
from helpers.clustering.clusterize import clusterize
from helpers.clustering.load_data import load_clustering_data
from helpers.clustering.data_featuring import data_featuring
    
def main():
    sidebar.display()
    
    our_df = load_clustering_data()
    
    with st.form("clustering_form"):
        st.markdown("### Công cụ phân loại nhà ở")
        
        st.number_input(key="dien_tich", label="Diện Tích", min_value=0.0)
        st.number_input(key="gia_ban", label="Giá Bán (tỷ VND)", min_value=0.0)
        st.number_input(key="so_phong_ngu", label="Số Phòng Ngủ", min_value=1.0)
        st.number_input(key="gia_kv_mean", label="Giá trung bình tại khu vực (tỷ VND)", min_value=0.0)
        st.text_area(key="mo_ta", label="Mô tả")
        st.selectbox(key="loai_hinh", label="Loại hình", options=our_df["loai_hinh"].value_counts().index.tolist())
        st.selectbox(key="quan", label="Quận", options=our_df["quan"].value_counts().index.tolist())
        
        submit = st.form_submit_button(key="clustering_submit", label="Đánh Giá")
        
        if submit:
            user_df = pd.DataFrame([st.session_state])
            user_df["full_text"] = user_df["mo_ta"]
            user_df = data_featuring(user_df)
                        
            clusterize_result = clusterize(user_df, our_df)
            st.write(f"Nhà ở được phân vào phân khúc {clusterize_result['cluster_name']}")
main()