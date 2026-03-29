import streamlit as st
import components.sidebar as sidebar
import components.post_card_list as post_card_list
import components.pagination as pagination
from features.recommendation.helpers.load_data import load_recommendation_data

def get_pagination_params():
    page_str = st.query_params.get("page", "0")
    page_size_str = st.query_params.get("page_size", "9")
    
    try:
        page = int(page_str)
    except ValueError:
        page = 0

    try:
        page_size = int(page_size_str)
    except ValueError:
        page_size = 9

    return page, page_size

def get_post_by_page(df, page, page_size):
    start = page * page_size
    end = start + page_size
    return df[start:end]

def main():
    st.set_page_config(page_title="Posts", layout="wide")
    
    sidebar.display()

    st.markdown(
        """
        <style>
            .posts-hero {
                border-radius: 18px;
                padding: 1.25rem 1.2rem;
                background: linear-gradient(120deg, #0f2027 0%, #203a43 52%, #2c5364 100%);
                color: #edf5ff;
                box-shadow: 0 14px 34px rgba(15, 32, 39, 0.22);
                margin-bottom: 1.2rem;
            }

            .posts-kicker {
                font-size: 0.8rem;
                letter-spacing: 0.12em;
                text-transform: uppercase;
                font-weight: 700;
                margin-bottom: 0.35rem;
                opacity: 0.92;
            }

            .posts-title {
                font-size: clamp(1.45rem, 2.1vw, 1.95rem);
                font-weight: 800;
                line-height: 1.25;
                margin-bottom: 0.45rem;
            }

            .posts-sub {
                font-size: 1rem;
                line-height: 1.55;
                opacity: 0.98;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="posts-hero">
            <div class="posts-kicker">Real Estate Listings</div>
            <div class="posts-title">🏠 Danh sách bài đăng mới nhất</div>
            <div class="posts-sub">
                Khám phá các bài đăng bất động sản mới nhất trên thị trường. 
                Duyệt qua danh sách các căn hộ, nhà phố, và đất nền được cập nhật liên tục 
                để tìm kiếm cơ hội đầu tư hoặc nơi an cư lý tưởng cho bạn và gia đình.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    page, page_size = get_pagination_params()
    df = load_recommendation_data()
    posts = get_post_by_page(df, page, page_size)
    
    post_card_list.display(posts)
    st.markdown("---")
    pagination.display(df, page, page_size)

if __name__ == "__main__":
    main()