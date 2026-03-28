import streamlit as st
import pandas as pd
import components.sidebar as sidebar


def main():
    st.set_page_config(page_title="Work Assignment", layout="wide")

    sidebar.display()

    st.markdown(
        """
        <style>
            .stApp {
                background: #ffffff;
            }

            header[data-testid="stHeader"] {
                background: #ffffff;
                border-bottom: 1px solid rgba(15, 32, 39, 0.1);
            }

            .ta-hero {
                border-radius: 18px;
                padding: 1.25rem 1.2rem;
                background: linear-gradient(120deg, #0f2027 0%, #203a43 52%, #2c5364 100%);
                color: #edf5ff;
                box-shadow: 0 14px 34px rgba(15, 32, 39, 0.22);
                margin-bottom: 1.2rem;
            }

            .ta-kicker {
                font-size: 0.8rem;
                letter-spacing: 0.12em;
                text-transform: uppercase;
                font-weight: 700;
                margin-bottom: 0.35rem;
                opacity: 0.92;
            }

            .ta-title {
                font-size: clamp(1.45rem, 2.1vw, 1.95rem);
                font-weight: 800;
                line-height: 1.25;
                margin-bottom: 0.45rem;
            }

            .ta-sub {
                font-size: 1rem;
                line-height: 1.55;
                opacity: 0.98;
            }

            .ta-section-title {
                margin-top: 1.25rem;
                margin-bottom: 0.7rem;
                font-size: 1.14rem;
                font-weight: 800;
                color: #142e3a;
            }

            .ta-note {
                border-radius: 12px;
                border: 1px solid rgba(15, 32, 39, 0.14);
                background: rgba(44, 83, 100, 0.06);
                padding: 0.85rem 0.95rem;
                color: #1f3f4f;
                line-height: 1.5;
                margin-top: 0.95rem;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="ta-hero">
            <div class="ta-kicker">Team Workflow</div>
            <div class="ta-title">📋 Phân công công việc</div>
            <div class="ta-sub">
                Bảng phân công thể hiện vai trò và tiến độ đóng góp của từng thành viên,
                bao gồm các hạng mục cốt lõi và phần mở rộng cộng điểm.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ===== DATA =====
    data = {
        "Công việc": [
            "Business Objective",
            "Data Understanding / Cleaning",
            "EDA & Feature Engineering",
            "Bài toán 1 — Recommendation System",
            "⭐ Bài toán 1 — Thuật toán BERT (cộng điểm)",
            "Bài toán 2 — Market Segmentation",
            "⭐ Bài toán 2 — Thuật toán Spectral (cộng điểm)",
            "Lên ý tưởng & Dựng GUI (Streamlit)"        
        ],
        "Quang": [
            "✔️", "✔️", "✔️", "✔️", "✔️",
            "", "", "✔️"
        ],
        "Quân": [
            "✔️", "✔️", "✔️", "",
            "", "✔️", "✔️", ""
        ]
    }

    df = pd.DataFrame(data)

    # ===== DISPLAY =====
    st.markdown('<div class="ta-section-title">🗂️ Bảng chi tiết</div>', unsafe_allow_html=True)
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
    )

    # ===== NOTE =====
    st.markdown(
        """
        <div class="ta-note">
            ⭐ <b>Ghi chú:</b><br/>
            - Các mục có dấu ⭐ là phần mở rộng / cộng điểm<br/>
            - Phân công dựa trên thế mạnh từng thành viên
        </div>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()
