import streamlit as st

def display():
    if "searched" not in st.session_state:
        st.session_state.searched = False
    
    query = st.text_input(
        "Tìm kiếm nhà",
        label_visibility="collapsed",
        key="search_query",
        placeholder="Tìm kiếm nhà...",
    )

    if query and not st.session_state.searched:
        st.session_state.final_query = query
        st.session_state.searched = True
        st.switch_page("pages/search_result.py")
