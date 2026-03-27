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
    st.markdown("## Kết quả tìm kiếm cho: " + query)
    st.markdown("---")

    recommended_posts = recommend_posts_by_query(query, df)
    post_card_list.display(recommended_posts)
    
    st.session_state.searched = False

main()