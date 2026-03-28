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
                background:
                    linear-gradient(165deg, #0f2027 0%, #203a43 52%, #2c5364 100%);
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
                color: #edf3fb;
            }

            section[data-testid="stSidebar"] hr {
                border-color: rgba(255, 255, 255, 0.18);
            }

            section[data-testid="stSidebar"] [data-testid="stTextInput"] input {
                background: rgba(255, 255, 255, 0.08);
                border: 1px solid rgba(255, 255, 255, 0.22);
                color: #f7fbff;
                font-size: 0.95rem;
            }

            section[data-testid="stSidebar"] [data-testid="stTextInput"] input::placeholder {
                color: #b7c6d8;
            }

            .sb-project-title {
                font-size: 1.72rem;
                font-weight: 700;
                line-height: 1.26;
                margin-top: 0.35rem;
                margin-bottom: 0.55rem;
                color: #f3f7fd;
            }

            .sb-top-banner {
                font-size: 32px;
                font-weight: 800;
                letter-spacing: 0.1em;
                text-transform: uppercase;
                color: #f4f8ff;
                margin-bottom: 0.25rem;
                padding-bottom: 0.42rem;
                # border-bottom: 1px solid rgba(255, 255, 255, 0.32);
            }

            .sb-search-label {
                font-size: 0.84rem;
                text-transform: uppercase;
                letter-spacing: 0.11em;
                color: #d8e6f5;
                font-weight: 700;
                margin-top: 0.15rem;
                margin-bottom: 0.22rem;
            }

            .sb-section-title {
                font-size: 0.84rem;
                text-transform: uppercase;
                letter-spacing: 0.11em;
                color: #d8e6f5;
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
                border-top: 1px solid rgba(255, 255, 255, 0.24);
            }

            .sb-footer {
                margin-top: 0.95rem;
                padding: 0;
                color: #e5edf7;
                font-size: 0.88rem;
                line-height: 1.45;
            }

            .sb-footer-divider {
                margin-top: 1rem;
                margin-bottom: 0.65rem;
                border-top: 1px solid rgba(255, 255, 255, 0.26);
            }

            .sb-footer strong {
                display: block;
                margin-bottom: 0.35rem;
                color: #f5f8fc;
            }

            .sb-footer em {
                color: #c8d5e4;
            }

            .sb-footer a {
                color: #b2d4ff;
                text-decoration: none;
                font-weight: 600;
            }

            .sb-footer a:hover {
                text-decoration: underline;
            }

            section[data-testid="stSidebar"] [data-testid="stPageLink"] a {
                border-radius: 0;
                padding-top: 0.12rem;
                padding-bottom: 0.12rem;
                padding-left: 0.1rem;
                color: #e5edf5;
                background: transparent;
                border: none;
                font-size: 0.98rem;
            }

            section[data-testid="stSidebar"] [data-testid="stPageLink"] {
                margin-bottom: 0.02rem;
            }

            section[data-testid="stSidebar"] [data-testid="stPageLink"] a:hover {
                background: transparent;
                color: #cde2ff;
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