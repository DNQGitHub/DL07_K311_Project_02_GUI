import streamlit as st
import components.search_input as search_input
import components.sidebar_post_list as sidebar_post_list
from features.recommendation.helpers.load_data import load_recommendation_data


SECTION_DIVIDER_HTML = '<div class="sb-section-divider"></div>'


def _inject_sidebar_styles():
    st.markdown(
        """
        <style>
            section[data-testid="stSidebar"] {
                border-right: 1px solid rgba(15, 32, 39, 0.08);
            }

            section[data-testid="stSidebar"] .block-container {
                padding-top: 1.2rem;
                padding-bottom: 1rem;
            }

            section[data-testid="stSidebar"] p,
            section[data-testid="stSidebar"] label,
            section[data-testid="stSidebar"] span,
            section[data-testid="stSidebar"] li,
            section[data-testid="stSidebar"] div {
                color: #142e3a;
            }

            section[data-testid="stSidebar"] hr {
                border-color: rgba(15, 32, 39, 0.12);
            }

            section[data-testid="stSidebar"] [data-testid="stTextInput"] div[data-baseweb="input"] {
                background: #f8fbfd !important;
                border: 1px solid rgba(15, 32, 39, 0.24) !important;
                border-radius: 8px !important;
                box-shadow: none !important;
            }

            section[data-testid="stSidebar"] [data-testid="stTextInput"] {
                margin-bottom: 0.3rem;
            }

            section[data-testid="stSidebar"] [data-testid="stTextInput"] div[data-baseweb="input"]:focus-within {
                border-color: rgba(15, 32, 39, 0.55) !important;
                box-shadow: 0 0 0 1px rgba(15, 32, 39, 0.15) !important;
            }

            section[data-testid="stSidebar"] [data-testid="stTextInput"] input {
                background: #f8fbfd !important;
                color: #0f2027 !important;
                -webkit-text-fill-color: #0f2027 !important;
                caret-color: #0f2027 !important;
                font-size: 0.95rem;
            }

            section[data-testid="stSidebar"] [data-testid="stTextInput"] input::placeholder {
                color: #6c7d8a !important;
                -webkit-text-fill-color: #6c7d8a !important;
            }

            .sb-project-title {
                font-size: 1.72rem;
                font-weight: 700;
                line-height: 1.26;
                margin-top: 0.35rem;
                margin-bottom: 0.55rem;
                color: #0f2027;
            }

            .sb-top-banner {
                font-size: 29px;
                font-weight: 800;
                letter-spacing: 0.1em;
                text-transform: uppercase;
                color: #0f2027;
                margin-bottom: 0.25rem;
                padding-bottom: 0.42rem;
                border-bottom: 1px solid rgba(15, 32, 39, 0.12);
            }

            .sb-search-label {
                font-size: 0.84rem;
                text-transform: uppercase;
                letter-spacing: 0.11em;
                color: #3a5361;
                font-weight: 700;
                margin-top: 0.15rem;
                margin-bottom: 0.22rem;
            }

            .sb-section-title {
                font-size: 0.84rem;
                text-transform: uppercase;
                letter-spacing: 0.11em;
                color: #3a5361;
                font-weight: 700;
                margin-top: 0.25rem;
                margin-bottom: 0.2rem;
            }

            .sb-post-title {
                margin-top: 0.55rem;
            }

            .sb-section-divider {
                margin-top: 0.55rem;
                margin-bottom: 0.45rem;
                border-top: 1px solid rgba(15, 32, 39, 0.14);
            }

            .sb-footer {
                margin-top: 0.95rem;
                padding: 0;
                color: #2a4454;
                font-size: 0.88rem;
                line-height: 1.45;
            }

            .sb-footer-divider {
                margin-top: 1rem;
                margin-bottom: 0.65rem;
                border-top: 1px solid rgba(15, 32, 39, 0.14);
            }

            .sb-footer strong {
                display: block;
                margin-bottom: 0.35rem;
                color: #0f2027;
            }

            .sb-footer em {
                color: #4e6877;
            }

            .sb-footer a {
                color: #1f5d8a;
                text-decoration: none;
                font-weight: 600;
            }

            .sb-footer a:hover {
                text-decoration: underline;
            }

            section[data-testid="stSidebar"] [data-testid="stPageLink"] a {
                border-radius: 6px;
                padding-top: 0.12rem;
                padding-bottom: 0.12rem;
                padding-left: 0.1rem;
                color: #17384b;
                background: transparent;
                border: none;
                font-size: 0.98rem;
            }

            section[data-testid="stSidebar"] [data-testid="stPageLink"] {
                margin-bottom: 0.02rem;
            }

            section[data-testid="stSidebar"] [data-testid="stPageLink"] a:hover {
                background: rgba(15, 32, 39, 0.06);
                color: #0f2027;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def display():
    df = load_recommendation_data()
    posts = df[:10]
    
    
    with st.sidebar:
        _inject_sidebar_styles()

        st.markdown('<div class="sb-top-banner">Project 02</div>', unsafe_allow_html=True)
        
        st.markdown(
            """
            <div class="sb-project-title">Đề xuất nhà dựa trên nội dung &amp; phân cụm nhà</div>
            """,
            unsafe_allow_html=True,
        )

        search_input.display()
        st.page_link(label="Trang Chủ", page="pages/home.py", use_container_width=True)
        st.page_link(label="Bối cảnh & Mục tiêu", page="pages/business_problem.py", use_container_width=True)
        st.page_link(label="Phân Công Nhiệm Vụ", page="pages/task_assignment.py", use_container_width=True)
        st.page_link(label="Phân Cụm Thị Trường", page="pages/market_clustering.py", use_container_width=True)
        st.page_link(label="Các Bài Đăng", page="pages/posts.py", use_container_width=True)
        
        st.markdown(SECTION_DIVIDER_HTML, unsafe_allow_html=True)
        st.markdown('<div class="sb-section-title sb-post-title">Các Bài Đăng</div>', unsafe_allow_html=True)
        sidebar_post_list.display(posts)
        
        st.markdown('<div class="sb-footer-divider"></div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="sb-footer">
                <strong>© 2026 - Nhóm 09</strong>
                Dự án đề xuất nhà dựa trên nội dung &amp; phân cụm nhà<br/>
                <em>GVHD: Thạc sỹ Khuất Thùy Phương</em><br/><br/>
                Thành Viên Nhóm:<br/>
                <a href="mailto:quan.phanngocminh111@gmail.com">Phan Ngọc Minh Quân</a><br/>
                <a href="mailto:dnq.httt@gmail.com">Đoàn Nhật Quang</a>
            </div>
            """,
            unsafe_allow_html=True,
        )