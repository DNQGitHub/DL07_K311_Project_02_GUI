import streamlit as st
import components.search_input as search_input
import pandas as pd

def display_post(row, index):
    tieu_de = row['tieu_de']
    tieu_de_short = tieu_de if len(tieu_de) <= 30 else tieu_de[:27] + "..."
    link = "/post_detail?post_id=" + str(index)
    st.html(f"""
        <a href='{link}' style='color: gray; font-size: 13px; padding: 0; padding-left: 1rem;'>{str(index + 1).rjust(2, "0")}. {tieu_de_short}</a>
    """)

def display_posts():
    df = pd.read_parquet("data/dataset_cleaned.parquet")
    container = st.container(gap=None)
    with container:
        for index, row in df.head(8).iterrows():
            display_post(row, index)


def display():
    with st.sidebar:
        st.image("https://picsum.photos/250/80", width=250)
        search_input.display()
        st.title("Project 02: Đề xuất nhà dựa trên nội dung & phân cụm nhà")
        st.page_link(label="Trang Chủ", page="pages/home.py")
        st.page_link(label="Vấn Đề Kinh Doanh", page="pages/business_problem.py")
        # st.page_link(label="Phân Công Nhiệm Vụ", page="pages/task_assignment.py")
        st.page_link(label="Các Bài Đăng", page="pages/posts.py")
        display_posts()