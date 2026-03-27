import streamlit as st
import components.sidebar_post as sidebar_post

def display(posts):
    container = st.container(gap=None)

    with container:
        for index, row in posts.iterrows():
            sidebar_post.display(row, index)