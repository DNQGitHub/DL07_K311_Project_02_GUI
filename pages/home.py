import streamlit as st
import components.sidebar as sidebar

def main():
    st.set_page_config(page_title="Home", layout="wide")
    
    sidebar.display()

    # ===== TITLE =====
    st.markdown("""
    # 📊 Ứng dụng Data Science trong Bất Động Sản

    Dự án tập trung xây dựng hệ thống:
    - 🔍 **Gợi ý bất động sản (Recommendation System)**
    - 📈 **Phân khúc thị trường (Market Segmentation)**

    Áp dụng trên dữ liệu thực tế từ nền tảng Nhà Tốt (Chợ Tốt).
    """)

    st.divider()

    # ===== OVERVIEW =====
    st.subheader("🚀 Nội dung chính")

    st.markdown("""
    **1. Business Problem**
    - Hiểu bài toán & dữ liệu
    - Xác định vấn đề cần giải quyết

    **2. Recommendation System**
    - Content-based Filtering
    - Hybrid (Text + Price + Location)

    **3. Market Segmentation**
    - KMeans, GMM, Agglomerative
    - Triển khai với Sklearn & PySpark

    **4. Demo hệ thống**
    - Tìm kiếm & gợi ý nhà tương tự
    """)

    st.divider()

    # ===== TECH STACK =====
    st.subheader("⚙️ Công nghệ sử dụng")

    st.markdown("""
    - **Python, Pandas, NumPy**
    - **Scikit-learn, Gensim**
    - **PySpark**
    - **Cosine Similarity**
    - **Streamlit (Dashboard)**
    """)

    st.divider()


if __name__ == "__main__":
    main()
