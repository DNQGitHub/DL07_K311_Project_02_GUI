import streamlit as st
import pandas as pd
import components.sidebar as sidebar
from features.clustering.helpers.clusterize import clusterize
from features.clustering.helpers.load_data import load_clustering_data
from features.clustering.helpers.data_featuring import data_featuring
    
def main():
    st.set_page_config(page_title="Market Clustering", layout="wide")
    
    sidebar.display()

    st.markdown(
        """
        <style>
            .stApp {
                background: #ffffff;
            }

            header[data-testid="stHeader"] {
                background: #ffffff;
                border-bottom: 1px solid rgba(15, 32, 39, 0.1);
            }

            .mc-hero {
                border-radius: 18px;
                padding: 1.25rem 1.2rem;
                background: linear-gradient(120deg, #0f2027 0%, #203a43 52%, #2c5364 100%);
                color: #edf5ff;
                box-shadow: 0 14px 34px rgba(15, 32, 39, 0.22);
                margin-bottom: 1.2rem;
            }

            .mc-kicker {
                font-size: 0.8rem;
                letter-spacing: 0.12em;
                text-transform: uppercase;
                font-weight: 700;
                margin-bottom: 0.35rem;
                opacity: 0.92;
            }

            .mc-title {
                font-size: clamp(1.45rem, 2.1vw, 1.95rem);
                font-weight: 800;
                line-height: 1.25;
                margin-bottom: 0.45rem;
            }

            .mc-sub {
                font-size: 1rem;
                line-height: 1.55;
                opacity: 0.98;
            }

            .mc-form-section {
                border-radius: 14px;
                border: 1px solid rgba(15, 32, 39, 0.12);
                background: rgba(255, 255, 255, 0.98);
                padding: 1.15rem 1.25rem;
                margin-top: 0.95rem;
            }

            .mc-result {
                border-radius: 14px;
                border: 2px solid rgba(15, 160, 100, 0.25);
                background: rgba(15, 160, 100, 0.06);
                padding: 1rem 1.15rem;
                color: #0a5a40;
                font-size: 1.05rem;
                font-weight: 600;
                margin-top: 1.5rem;
                text-align: center;
            }

            /* Button styling - more aggressive selectors */
            div[data-testid="stFormSubmitButton"] button {
                background: linear-gradient(135deg, #ff6b35 0%, #ff4757 100%) !important;
                color: #ffffff !important;
                box-shadow: 0 10px 30px rgba(255, 71, 87, 0.4) !important;
                border: none !important;
                font-weight: 900 !important;
                font-size: 1.3rem !important;
                padding: 1.2rem 1.5rem !important;
                letter-spacing: 0.1em !important;
                transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
                text-transform: uppercase !important;
                border-radius: 8px !important;
            }

            div[data-testid="stFormSubmitButton"] button:hover {
                box-shadow: 0 16px 40px rgba(255, 71, 87, 0.6) !important;
                transform: translateY(-4px) !important;
                background: linear-gradient(135deg, #ff7f50 0%, #ff6b6b 100%) !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="mc-hero">
            <div class="mc-kicker">Market Intelligence</div>
            <div class="mc-title">🏘️ Phân khúc thị trường</div>
            <div class="mc-sub">
                Sử dụng công cụ phân loại để xác định phân khúc thích hợp của bất động sản.
                Nhập thông tin chi tiết để nhận kết quả phân loại.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    our_df = load_clustering_data()
    
    with st.form("clustering_form"):
        st.markdown('<div style="font-size: 1.14rem; font-weight: 800; color: #142e3a; margin-bottom: 0.7rem;">📝 Thông tin nhà ở</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.number_input(key="dien_tich", label="Diện Tích", min_value=0.0)
            st.number_input(key="gia_ban", label="Giá Bán (tỷ VND)", min_value=0.0)
            st.number_input(key="so_phong_ngu", label="Số Phòng Ngủ", min_value=1.0)
        
        with col2:
            st.number_input(key="gia_kv_mean", label="Giá trung bình tại khu vực (tỷ VND)", min_value=0.0)
            st.selectbox(key="loai_hinh", label="Loại hình", options=our_df["loai_hinh"].value_counts().index.tolist())
            st.selectbox(key="quan", label="Quận", options=our_df["quan"].value_counts().index.tolist())
        
        st.text_area(key="mo_ta", label="Mô tả", height=100)
        
        submit = st.form_submit_button(key="clustering_submit", label="Đánh Giá", use_container_width=True)
        
        if submit:
            user_df = pd.DataFrame([st.session_state])
            user_df["full_text"] = user_df["mo_ta"]
            user_df = data_featuring(user_df)
                        
            result = clusterize(user_df, our_df)
            st.session_state.clustering_result = result
            
    # Display result outside form
    if "clustering_result" in st.session_state and st.session_state.clustering_result:
        st.markdown(
            f'<div class="mc-result">✨ Nhà ở được phân vào phân khúc <b>{st.session_state.clustering_result["cluster_name"]}</b></div>',
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()