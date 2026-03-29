import streamlit as st
import components.sidebar as sidebar


def main():
    st.set_page_config(page_title="Business Problem", layout="wide")

    sidebar.display()

    st.markdown(
        """
        <style>
            .bp-hero {
                border-radius: 18px;
                padding: 1.35rem 1.25rem;
                background: linear-gradient(120deg, #0f2027 0%, #203a43 52%, #2c5364 100%);
                color: #edf5ff;
                box-shadow: 0 14px 34px rgba(15, 32, 39, 0.22);
                margin-bottom: 1.35rem;
            }

            .bp-kicker {
                font-size: 0.8rem;
                letter-spacing: 0.12em;
                text-transform: uppercase;
                font-weight: 700;
                margin-bottom: 0.35rem;
                opacity: 0.92;
            }

            .bp-title {
                font-size: clamp(1.45rem, 2.1vw, 2rem);
                font-weight: 800;
                line-height: 1.25;
                margin-bottom: 0.45rem;
            }

            .bp-sub {
                font-size: 1rem;
                line-height: 1.55;
                opacity: 0.98;
            }

            .bp-section-title {
                margin-top: 1.3rem;
                margin-bottom: 0.75rem;
                font-size: 1.16rem;
                font-weight: 800;
                color: #142e3a;
            }

            .bp-card {
                border-radius: 14px;
                padding: 1rem 1.05rem;
                background: #ffffff;
                border: 1px solid rgba(15, 32, 39, 0.12);
                box-shadow: 0 8px 20px rgba(15, 32, 39, 0.08);
            }

            .bp-card-context {
                min-height: 220px;
            }

            .bp-card-goal {
                min-height: 250px;
            }

            .bp-card-title {
                font-size: 1.02rem;
                font-weight: 800;
                color: #1c3c4a;
                margin-bottom: 0.45rem;
            }

            .bp-footer {
                margin-top: 1.5rem;
                padding-top: 0.75rem;
                border-top: 1px solid rgba(15, 32, 39, 0.14);
                color: #4a5f69;
                font-size: 0.9rem;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="bp-hero">
            <div class="bp-kicker">Project Context</div>
            <div class="bp-title">📊 Bối cảnh &amp; Mục tiêu</div>
            <div class="bp-sub">
                Bài toán tập trung vào hai trục chính: Recommendation System và Market Segmentation,
                xây dựng trên dữ liệu nhà ở thực tế từ nền tảng Nhà Tốt.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="bp-section-title">🏠 Bối cảnh</div>', unsafe_allow_html=True)
    left_col, right_col = st.columns([1.1, 1])

    with left_col:
        st.markdown(
            """
            <div class="bp-card bp-card-context">
                <div class="bp-card-title">Dữ liệu đầu vào</div>
                <b>Nhà Tốt (nhatot.com)</b><br/>
                Nền tảng BĐS thuộc Chợ Tốt - mua bán trực tuyến hàng đầu Việt Nam<br/><br/>
                <b>Dữ liệu:</b><br/>
                - 8,273 tin đăng nhà riêng lẻ<br/>
                - Khu vực: Bình Thạnh, Gò Vấp, Phú Nhuận (TP.HCM)
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right_col:
        st.markdown(
            """
            <div class="bp-card bp-card-context">
                <div class="bp-card-title">Vấn đề hiện tại</div>
                - Chưa có hệ thống gợi ý nhà tương tự<br/>
                - Chưa thực hiện phân khúc thị trường nhà ở
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown('<div class="bp-section-title">🎯 Mục tiêu</div>', unsafe_allow_html=True)
    rec_col, seg_col = st.columns(2)

    with rec_col:
        st.markdown(
            """
            <div class="bp-card bp-card-goal">
                <div class="bp-card-title">1. Recommendation System</div>
                <b>Content-based:</b><br/>
                - Cosine Similarity<br/>
                - Gensim LSI<br/><br/>
                <b>Hybrid:</b><br/>
                - Text + Price + Location Similarity
            </div>
            """,
            unsafe_allow_html=True,
        )

    with seg_col:
        st.markdown(
            """
            <div class="bp-card bp-card-goal">
                <div class="bp-card-title">2. Market Segmentation</div>
                <b>Sklearn:</b><br/>
                - KMeans<br/>
                - GMM<br/>
                - Agglomerative Clustering<br/><br/>
                <b>PySpark:</b><br/>
                - KMeans<br/>
                - GMM<br/>
                - Bisecting K-Means
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        '<div class="bp-footer">Data Science Process - Sklearn + PySpark - Gensim + Cosine Similarity</div>',
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
