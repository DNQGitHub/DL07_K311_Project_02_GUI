import streamlit as st
import components.sidebar as sidebar
import components.post_card as post_card
import components.pagination as pagination
import pandas as pd
from helpers.load_data import load_data

def show_posts(df, page=0, page_size=9):
    start = page * page_size
    end = start + page_size

    st.html(f"<h2 style='text-align: center;'>Các Bài Đăng</h2>")
    
    
    for index, row in df[start:end].iterrows():
        post_card.display(row, index)

def main():
    page = int(st.query_params.get("page", 0))
    page_size = int(st.query_params.get("page_size", 9))

    sidebar.display()
    df = load_data()
    df.info()
    show_posts(df, page, page_size)
    st.markdown("---")
    pagination.display(df, page, page_size)

main()