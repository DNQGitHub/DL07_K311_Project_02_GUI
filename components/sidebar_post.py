import streamlit as st

def display(post, index):
    tieu_de = post['tieu_de']
    tieu_de_short = tieu_de if len(tieu_de) <= 30 else tieu_de[:27] + "..."
    link = "/post_detail?post_id=" + str(index)

    st.html(f"""
        <a
            href='{link}'
            style='
                display: block;
                color: #f1f6ff;
                font-size: 14px;
                padding: 0.1rem 0 0.1rem 0.1rem;
                margin: 0.03rem 0;
                border-radius: 0;
                text-decoration: none;
                background: transparent;
                border: none;
            '
        >
            <span style='font-weight: 700; color: #b7d4ff;'>{str(index + 1).rjust(2, "0")}</span>
            <span>. {tieu_de_short}</span>
        </a>
    """)