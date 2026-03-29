import streamlit as st
import components.sidebar as sidebar


TECH_STACK = [
    "Python",
    "Pandas",
    "NumPy",
    "Scikit-learn",
    "Gensim",
    "PySpark",
    "Cosine Similarity",
    "Streamlit Dashboard",
]


def _inject_styles():
    st.markdown(
        """
        <style>
            .home-hero {
                border-radius: 18px;
                padding: 1.5rem 1.4rem;
                background: linear-gradient(120deg, #0f2027 0%, #203a43 52%, #2c5364 100%);
                color: #ecf5ff;
                box-shadow: 0 14px 34px rgba(15, 32, 39, 0.24);
                margin-bottom: 1.5rem;
            }

            .home-kicker {
                font-size: 0.8rem;
                letter-spacing: 0.12em;
                text-transform: uppercase;
                font-weight: 700;
                opacity: 0.9;
                margin-bottom: 0.45rem;
            }

            .home-title {
                font-size: clamp(1.5rem, 2.2vw, 2.2rem);
                font-weight: 800;
                line-height: 1.25;
                margin-bottom: 0.55rem;
            }

            .home-sub {
                font-size: 1rem;
                line-height: 1.55;
                opacity: 0.97;
            }

            .home-card {
                border-radius: 14px;
                padding: 0.95rem 1rem;
                background: #ffffff;
                border: 1px solid rgba(15, 32, 39, 0.1);
                box-shadow: 0 8px 20px rgba(15, 32, 39, 0.08);
                height: 100%;
            }

            .home-card-title {
                font-size: 0.85rem;
                text-transform: uppercase;
                letter-spacing: 0.08em;
                font-weight: 700;
                color: #33505e;
                margin-bottom: 0.35rem;
            }

            .home-card-value {
                font-size: 1.45rem;
                font-weight: 800;
                color: #102630;
                margin-bottom: 0.2rem;
            }

            .home-card-desc {
                font-size: 0.92rem;
                color: #3a4e57;
                line-height: 1.45;
            }

            .section-title {
                margin-top: 1.45rem;
                margin-bottom: 0.8rem;
                font-size: 1.2rem;
                font-weight: 800;
                color: #152f3b;
            }

            .roadmap-card {
                border-left: 5px solid #2c5364;
            }

            .spacious-block {
                margin-bottom: 1.1rem;
            }

            .tech-wrap {
                display: flex;
                flex-wrap: wrap;
                gap: 0.5rem;
            }

            .tech-chip {
                padding: 0.4rem 0.7rem;
                border-radius: 999px;
                font-size: 0.85rem;
                font-weight: 700;
                color: #0f2027;
                background: linear-gradient(120deg, rgba(44, 83, 100, 0.2), rgba(96, 125, 139, 0.22));
                border: 1px solid rgba(15, 32, 39, 0.15);
            }

        </style>
        """,
        unsafe_allow_html=True,
    )


def _render_variant_hero_cards():
    st.markdown(
        """
        <div class="home-hero">
            <div class="home-kicker">Data Science Application</div>
            <div class="home-title">📊 Ứng dụng Data Science trong Bất Động Sản</div>
            <div class="home-sub">
                Dự án tập trung xây dựng hệ thống gợi ý bất động sản và phân khúc thị trường,
                áp dụng trên dữ liệu thực tế từ nền tảng Nhà Tốt (Chợ Tốt).
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-title">🎯 Trọng tâm dự án</div>', unsafe_allow_html=True)
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Business Problem", "01")
    m2.metric("Recommendation", "02")
    m3.metric("Segmentation", "03")
    m4.metric("Demo", "04")

    st.markdown('<div class="spacious-block"></div>', unsafe_allow_html=True)


def _render_shared_content():
    st.markdown('<div class="section-title">🚀 Nội dung chính</div>', unsafe_allow_html=True)
    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown(
            """
            <div class="home-card roadmap-card spacious-block">
                <b>1. Business Problem</b><br/>
                - Hiểu bài toán &amp; dữ liệu<br/>
                - Xác định vấn đề cần giải quyết<br/><br/>
                <b>2. Recommendation System</b><br/>
                - Content-based Filtering<br/>
                - Hybrid (Text + Price + Location)
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_right:
        st.markdown(
            """
            <div class="home-card roadmap-card spacious-block">
                <b>3. Market Segmentation</b><br/>
                - KMeans, GMM, Agglomerative<br/>
                - Triển khai với Sklearn &amp; PySpark<br/><br/>
                <b>4. Demo hệ thống</b><br/>
                - Tìm kiếm &amp; gợi ý nhà tương tự
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown('<div class="section-title">⚙️ Công nghệ sử dụng</div>', unsafe_allow_html=True)
    chips_html = "".join(f'<span class="tech-chip">{item}</span>' for item in TECH_STACK)
    st.markdown(f'<div class="tech-wrap">{chips_html}</div>', unsafe_allow_html=True)


def main():
    st.set_page_config(page_title="Home", layout="wide")

    sidebar.display()

    _inject_styles()
    _render_variant_hero_cards()

    _render_shared_content()


if __name__ == "__main__":
    main()
