import streamlit as st

def display(df, page, page_size):
    total_pages = (len(df) - 1) // page_size + 1
    disable_prev = page <= 0
    disable_next = page >= total_pages - 1
    
    st.html(f"""
        <div style="display: flex; align-items: center; justify-content: space-between; gap: 10px; padding: 10px; border-radius: 5px; margin-bottom: 10px;">
            <a href="?page={page - 1}" style="color: {'gray' if disable_prev else 'blue'}; text-decoration: underline; pointer-events: {'none' if disable_prev else 'auto'};">Previous</a>
            <a href="?page={page + 1}" style="color: {'gray' if disable_next else 'blue'}; text-decoration: underline; pointer-events: {'none' if disable_next else 'auto'};">Next</a>
        </div>
    """)
