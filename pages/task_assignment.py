import streamlit as st
import pandas as pd
import components.sidebar as sidebar

def main():
    st.set_page_config(page_title="Work Assignment")

    sidebar.display()

    st.title("📋 Phân công công việc")
    st.divider()

    # ===== DATA =====
    data = {
        "Công việc": [
            "Business Objective",
            "Data Understanding / Cleaning",
            "EDA & Feature Engineering",
            "Bài toán 1 — Recommendation System",
            "⭐ Bài toán 1 — Thuật toán BM25 (cộng điểm)",
            "Bài toán 2 — Market Segmentation",
            "⭐ Bài toán 2 — Thuật toán Spectral (cộng điểm)",
            "Dựng GUI (Streamlit)",
            "Lên ý tưởng & thiết kế hệ thống"
        ],
        "Quang": [
            "✔️", "✔️", "✔️", "✔️", "✔️",
            "", "", "✔️", "✔️"
        ],
        "Quân": [
            "✔️", "✔️", "✔️", "",
            "", "✔️", "✔️", "", ""
        ]
    }

    df = pd.DataFrame(data)

    # ===== DISPLAY =====
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # ===== NOTE =====
    st.markdown("""
    ⭐ **Ghi chú:**
    - Các mục có dấu ⭐ là phần mở rộng / cộng điểm
    - Phân công dựa trên thế mạnh từng thành viên
    """)

main()
