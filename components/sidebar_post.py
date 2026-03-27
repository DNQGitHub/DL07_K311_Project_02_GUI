import streamlit as st

def display(post, index):
    tieu_de = post['tieu_de']
    tieu_de_short = tieu_de if len(tieu_de) <= 30 else tieu_de[:27] + "..."
    link = "/post_detail?post_id=" + str(index)

    st.html(f"""
        <a href='{link}' style='color: gray; font-size: 13px; padding: 0; padding-left: 1rem;'>{str(index + 1).rjust(2, "0")}. {tieu_de_short}</a>
    """)