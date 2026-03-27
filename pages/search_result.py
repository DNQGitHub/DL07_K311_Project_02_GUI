import streamlit as st
import components.sidebar as sidebar
import components.post_card_list as post_card_list
from helpers.load_data import load_data
from helpers.recommendation.recommend_posts_by_query import recommend_posts_by_query

def main():
    if "searched" not in st.session_state:
        st.session_state.searched = False
    
    sidebar.display()
    df = load_data()
    
    query = st.session_state.get("final_query", "")
    
    if not query:
        st.markdown("## Chào mừng bạn đến với ứng dụng tìm kiếm bất động sản!")
        st.markdown("Vui lòng nhập truy vấn tìm kiếm trên thanh bên trái.")
        st.session_state.searched = False
        return

    st.markdown("## Top 5 kết quả tìm kiếm cho: ")
    st.html(f"<p style='font-size: 20px; color: #007bff;'>{query}</p>")
    st.markdown("---")

    recommended_posts = recommend_posts_by_query(query, df)
    post_card_list.display(recommended_posts)
    
    st.session_state.searched = False

main()