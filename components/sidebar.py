import streamlit as st
import components.search_input as search_input
import components.sidebar_post_list as sidebar_post_list
from features.recommendation.helpers.load_data import load_recommendation_data

def display():
    df = load_recommendation_data()
    posts = df[:10]
    
    
    with st.sidebar:
        st.image("https://picsum.photos/250/80", width=250)
        
        search_input.display()
        
        st.title("Project 02: Đề xuất nhà dựa trên nội dung & phân cụm nhà")
        
        st.page_link(label="Trang Chủ", page="pages/home.py")
        st.page_link(label="Bối cảnh & Mục tiêu", page="pages/business_problem.py")
        st.page_link(label="Phân Công Nhiệm Vụ", page="pages/task_assignment.py")
        st.page_link(label="Phân Cụm Thị Trường", page="pages/market_clustering.py")
        st.page_link(label="Các Bài Đăng", page="pages/posts.py")
        
        sidebar_post_list.display(posts)