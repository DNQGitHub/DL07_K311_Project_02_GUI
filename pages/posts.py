import streamlit as st
import components.sidebar as sidebar
import components.post_card as post_card
import components.post_card_list as post_card_list
import components.pagination as pagination
from helpers.load_data import load_data

def main():
    page = int(st.query_params.get("page", 0))
    page_size = int(st.query_params.get("page_size", 9))
    df = load_data()
    
    start = page * page_size
    end = start + page_size
    posts = df[start:end]
    
    # ---------------

    sidebar.display()
    st.html("<h2 style='text-align: center;'>Các Bài Đăng</h2>")
    post_card_list.display(posts)
    st.markdown("---")
    pagination.display(df, page, page_size)

main()