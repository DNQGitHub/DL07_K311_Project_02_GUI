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
    sidebar.display()

    st.markdown("## Các bài đăng bất động sản mới nhất trên thị trường")
    st.markdown("Khám phá các bài đăng bất động sản mới nhất trên thị trường. Duyệt qua danh sách các căn hộ, nhà phố, và đất nền được cập nhật liên tục để tìm kiếm cơ hội đầu tư hoặc nơi an cư lý tưởng cho bạn và gia đình.")
    
    page, page_size = get_pagination_params()
    df = load_recommendation_data()
    posts = get_post_by_page(df, page, page_size)
    
    post_card_list.display(posts)
    st.markdown("---")
    pagination.display(df, page, page_size)

main()