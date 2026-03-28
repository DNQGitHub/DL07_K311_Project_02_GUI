import streamlit as st
import components.sidebar as sidebar
import components.post_card_list as post_card_list
from features.recommendation.helpers.load_data import load_recommendation_data
from features.recommendation.helpers.recommend_posts_by_query import recommend_posts_by_query

def main():
    st.set_page_config(page_title="Search Result", layout="wide")
    
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

            .sr-hero {
                border-radius: 18px;
                padding: 1.25rem 1.2rem;
                background: linear-gradient(120deg, #0f2027 0%, #203a43 52%, #2c5364 100%);
                color: #edf5ff;
                box-shadow: 0 14px 34px rgba(15, 32, 39, 0.22);
                margin-bottom: 1.2rem;
            }

            .sr-kicker {
                font-size: 0.8rem;
                letter-spacing: 0.12em;
                text-transform: uppercase;
                font-weight: 700;
                margin-bottom: 0.35rem;
                opacity: 0.92;
            }

            .sr-title {
                font-size: clamp(1.45rem, 2.1vw, 1.95rem);
                font-weight: 800;
                line-height: 1.25;
                margin-bottom: 0.45rem;
            }

            .sr-sub {
                font-size: 1rem;
                line-height: 1.55;
                opacity: 0.98;
            }

            .sr-query {
                font-size: 1.25rem;
                font-weight: 800;
                color: #0f2027;
                margin: 0;
                word-break: break-word;
            }

            .sr-query-highlight {
                background: linear-gradient(120deg, #0f2027 0%, #203a43 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }

            .sr-results-header {
                margin-top: 1rem;
                margin-bottom: 1.5rem;
                padding-bottom: 1rem;
                border-bottom: 2px solid rgba(15, 32, 39, 0.1);
            }

            .sr-empty {
                text-align: center;
                padding: 3rem 1rem;
                color: #556770;
            }

            .sr-empty-icon {
                font-size: 3rem;
                margin-bottom: 1rem;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    if "searched" not in st.session_state:
        st.session_state.searched = False
    
    sidebar.display()
    df = load_recommendation_data()
    
    query = st.session_state.get("final_query", "")
    
    if not query:
        st.markdown(
            """
            <div class="sr-hero">
                <div class="sr-kicker">Search Real Estate</div>
                <div class="sr-title">🔍 Tìm kiếm bất động sản</div>
                <div class="sr-sub">
                    Vui lòng nhập truy vấn tìm kiếm trên thanh bên trái để bắt đầu.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.session_state.searched = False
        return

    st.markdown(
        """
        <div class="sr-hero">
            <div class="sr-kicker">Search Results</div>
            <div class="sr-title">🔍 Kết quả tìm kiếm</div>
            <div class="sr-sub">
                Các bất động sản phù hợp nhất với truy vấn của bạn
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="sr-results-header">
            <p class="sr-query">Kết quả cho: <span class="sr-query-highlight">"{query}"</span></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    recommended_posts = recommend_posts_by_query(query, df)
    
    if len(recommended_posts) == 0:
        st.markdown(
            """
            <div class="sr-empty">
                <div class="sr-empty-icon">🔎</div>
                <p style="font-size: 1.1rem; font-weight: 600; color: #142e3a;">Tidak tìm thấy kết quả</p>
                <p>Hãy thử lại với từ khóa khác</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        post_card_list.display(recommended_posts)
    
    st.session_state.searched = False

if __name__ == "__main__":
    main()