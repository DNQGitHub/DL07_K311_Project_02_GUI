import streamlit as st
import components.sidebar as sidebar
import components.single_clustering_form as single_clustering_form
import components.multiple_clustering_form as multiple_clustering_form
from features.clustering.helpers.load_data import load_clustering_data


def main():
    st.set_page_config(page_title="Market Clustering", layout="wide")

    sidebar.display()

    st.markdown(
        """
        <style>
            .mc-hero {
                border-radius: 18px;
                padding: 1.25rem 1.2rem;
                background: linear-gradient(120deg, #0f2027 0%, #203a43 52%, #2c5364 100%);
                color: #edf5ff;
                box-shadow: 0 14px 34px rgba(15, 32, 39, 0.22);
                margin-bottom: 1.2rem;
            }
            .mc-kicker {
                font-size: 0.8rem;
                letter-spacing: 0.12em;
                text-transform: uppercase;
                font-weight: 700;
                margin-bottom: 0.35rem;
                opacity: 0.92;
            }
            .mc-title {
                font-size: clamp(1.45rem, 2.1vw, 1.95rem);
                font-weight: 800;
                line-height: 1.25;
                margin-bottom: 0.45rem;
            }
            .mc-sub {
                font-size: 1rem;
                line-height: 1.55;
                opacity: 0.98;
            }
            div[data-testid="stForm"] div[data-baseweb="input"],
            div[data-testid="stForm"] div[data-baseweb="select"] > div,
            div[data-testid="stForm"] textarea {
                background: #f8fbfd !important;
                border-color: rgba(15, 32, 39, 0.14) !important;
                box-shadow: none !important;
            }
            div[data-testid="stForm"] input,
            div[data-testid="stForm"] textarea {
                background: #f8fbfd !important;
                color: #0f2027 !important;
                -webkit-text-fill-color: #0f2027 !important;
            }
            div[data-testid="stForm"] [data-testid="stNumberInputStepUp"],
            div[data-testid="stForm"] [data-testid="stNumberInputStepDown"] {
                background: #f8fbfd !important;
                border-left: 1px solid rgba(15, 32, 39, 0.14) !important;
                color: #0f2027 !important;
            }
            div[data-testid="stFormSubmitButton"] button {
                background: linear-gradient(135deg, #ff6b35 0%, #ff4757 100%) !important;
                color: #ffffff !important;
                box-shadow: 0 10px 30px rgba(255, 71, 87, 0.4) !important;
                border: none !important;
                font-weight: 900 !important;
                font-size: 1.3rem !important;
                padding: 1.2rem 1.5rem !important;
                letter-spacing: 0.1em !important;
                transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
                text-transform: uppercase !important;
                border-radius: 8px !important;
            }
            div[data-testid="stFormSubmitButton"] button:hover {
                box-shadow: 0 16px 40px rgba(255, 71, 87, 0.6) !important;
                transform: translateY(-4px) !important;
                background: linear-gradient(135deg, #ff7f50 0%, #ff6b6b 100%) !important;
            }
            div[data-testid="stBaseButton-primary"] button,
            button[data-testid="stBaseButton-primary"] {
                background: linear-gradient(135deg, #ff6b35 0%, #ff4757 100%) !important;
                color: #ffffff !important;
                box-shadow: 0 10px 30px rgba(255, 71, 87, 0.4) !important;
                border: none !important;
                font-weight: 900 !important;
                font-size: 1.3rem !important;
                padding: 1.2rem 1.5rem !important;
                letter-spacing: 0.1em !important;
                transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
                text-transform: uppercase !important;
                border-radius: 8px !important;
            }
            div[data-testid="stBaseButton-primary"] button:hover,
            button[data-testid="stBaseButton-primary"]:hover {
                box-shadow: 0 16px 40px rgba(255, 71, 87, 0.6) !important;
                transform: translateY(-4px) !important;
                background: linear-gradient(135deg, #ff7f50 0%, #ff6b6b 100%) !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="mc-hero">
            <div class="mc-kicker">Market Intelligence</div>
            <div class="mc-title">🏘️ Phân khúc thị trường</div>
            <div class="mc-sub">
                Sử dụng công cụ phân loại để xác định phân khúc thích hợp của bất động sản.
                Nhập thông tin chi tiết để nhận kết quả phân loại.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    our_df = load_clustering_data()

    tab1, tab2 = st.tabs(["📊 Đánh Giá 1 Nhà", "📁 Đánh Giá Hàng Loạt"])

    with tab1:
        single_clustering_form.render(our_df)

    with tab2:
        multiple_clustering_form.render(our_df)


if __name__ == "__main__":
    main()
