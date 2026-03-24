import streamlit as st

def display():
    with st.sidebar:
        st.image("https://picsum.photos/250/80", width=250)
        st.title("Project 2: Đề xuất nhà dựa trên nội dung & phân cụm nhà")
        st.page_link(label="Home", page="pages/home.py")
        st.page_link(label="Business Problem", page="pages/business_problem.py")
        st.page_link(label="Task Assignment", page="pages/task-assignment.py")