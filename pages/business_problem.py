import streamlit as st
import components.sidebar as sidebar

def main():
    st.set_page_config(page_title="Business Problem", layout="wide")

    sidebar.display()

    # ===== TITLE =====
    st.title("📊 Bối cảnh & Mục tiêu")
    st.divider()

    # ===== BỐI CẢNH =====
    st.header("🏠 Bối cảnh")

    st.markdown("""
    **Nhà Tốt (nhatot.com)**  
    Nền tảng BĐS thuộc Chợ Tốt — mua bán trực tuyến hàng đầu Việt Nam  

    **Dữ liệu:**  
    - 8,273 tin đăng nhà riêng lẻ  
    - Khu vực: Bình Thạnh, Gò Vấp, Phú Nhuận (TP.HCM)

    **Vấn đề hiện tại:**  
    - Chưa có hệ thống gợi ý nhà tương tự  
    - Chưa thực hiện phân khúc thị trường nhà ở
    """)

    st.info("📌 Hiện tại chưa có hệ thống Recommendation & Market Segmentation")

    st.divider()

    # ===== MỤC TIÊU =====
    st.header("🎯 Mục tiêu")

    # --- Bài toán 1 ---
    st.subheader("1. Recommendation System")

    st.markdown("""
    **Content-based:**
    - Cosine Similarity  
    - Gensim LSI  

    **Hybrid:**
    - Text + Price + Location Similarity  
    """)

    # --- Bài toán 2 ---
    st.subheader("2. Market Segmentation")

    st.markdown("""
    **Sklearn:**
    - KMeans  
    - GMM  
    - Agglomerative Clustering  

    **PySpark:**
    - KMeans  
    - GMM  
    - Bisecting K-Means  
    """)

    st.success("🎯 Mục tiêu: Xây dựng hệ thống gợi ý & phân khúc thị trường nhà ở")

    st.divider()

    # ===== FOOTER =====
    st.caption("Data Science Process — Sklearn + PySpark — Gensim + Cosine Similarity")


if __name__ == "__main__":
    main()
