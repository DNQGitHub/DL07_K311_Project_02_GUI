import streamlit as st

def display():
    with st.sidebar:
        st.image("https://picsum.photos/250/80", width=250)
        st.title("Project 02: Đề xuất nhà dựa trên nội dung & phân cụm nhà")
        st.page_link(label="Trang Chủ", page="pages/home.py")
        st.page_link(label="Vấn Đề Kinh Doanh", page="pages/business_problem.py")
        st.page_link(label="Phân Công Nhiệm Vụ", page="pages/task_assignment.py")
        st.page_link(label="Các Bài Đăng", page="pages/posts.py")