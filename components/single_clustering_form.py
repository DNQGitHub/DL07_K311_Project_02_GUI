import streamlit as st
import pandas as pd
from features.clustering.helpers.clusterize import clusterize
from features.clustering.helpers.data_featuring import data_featuring


def render(our_df):
    """Render form đánh giá phân khúc cho 1 bất động sản."""

    if "clustering_processing" not in st.session_state:
        st.session_state.clustering_processing = False

    with st.form("clustering_form"):
        st.markdown(
            '<div style="font-size: 1.14rem; font-weight: 800; color: #142e3a; margin-bottom: 0.7rem;">📝 Thông tin nhà ở</div>',
            unsafe_allow_html=True,
        )

        col1, col2 = st.columns(2)
        with col1:
            st.number_input(key="dien_tich", label="Diện Tích (m²)", min_value=0.0)
            st.number_input(key="gia_ban", label="Giá Bán (tỷ VND)", min_value=0.0)
            st.number_input(key="so_phong_ngu", label="Số Phòng Ngủ", min_value=1.0)
        with col2:
            st.number_input(
                key="gia_kv_mean",
                label="Giá TB khu vực (tỷ VND)",
                min_value=0.0,
            )
            st.selectbox(
                key="loai_hinh",
                label="Loại hình",
                options=our_df["loai_hinh"].value_counts().index.tolist(),
            )
            st.selectbox(
                key="quan",
                label="Quận",
                options=our_df["quan"].value_counts().index.tolist(),
            )

        st.text_area(key="mo_ta", label="Mô tả", height=100)

        btn_label = "⏳ Đang xử lý..." if st.session_state.clustering_processing else "Đánh Giá"
        submit = st.form_submit_button(
            label=btn_label,
            disabled=st.session_state.clustering_processing,
            use_container_width=True,
        )

    if submit and not st.session_state.clustering_processing:
        st.session_state.clustering_processing = True
        st.rerun()

    if st.session_state.clustering_processing:
        user_df = pd.DataFrame([st.session_state])
        user_df["full_text"] = user_df["mo_ta"]
        user_df = data_featuring(user_df)
        result = clusterize(user_df, our_df)
        st.session_state.clustering_result = result
        st.session_state.clustering_processing = False
        st.rerun()

    if "clustering_result" in st.session_state and st.session_state.clustering_result:
        _render_result_card(st.session_state.clustering_result)


def _render_result_card(result):
    labels_meta = {
        "Bình dân": {"color": "#1e6b3e", "bg": "rgba(233,255,244,0.92)", "border": "rgba(15,160,100,0.24)"},
        "Cao cấp":  {"color": "#1a4a8a", "bg": "rgba(235,244,255,0.92)", "border": "rgba(15,80,200,0.24)"},
    }
    name = result["cluster_name"]
    meta = labels_meta.get(name, {"color": "#0c5841", "bg": "rgba(233,255,244,0.92)", "border": "rgba(15,160,100,0.24)"})

    st.markdown(
        f"""
        <div style="
            margin-top: 1.55rem;
            border-radius: 16px;
            border: 1px solid {meta['border']};
            background: linear-gradient(135deg, {meta['bg']} 0%, #fff 100%);
            box-shadow: 0 12px 26px rgba(0,0,0,0.08);
            padding: 1.4rem 1.5rem;
            text-align: center;
            color: {meta['color']};
        ">
            <div style="
                display: inline-block;
                background: rgba(0,0,0,0.06);
                border-radius: 999px;
                font-size: 0.75rem;
                font-weight: 800;
                letter-spacing: 0.1em;
                text-transform: uppercase;
                padding: 0.28rem 0.8rem;
                margin-bottom: 0.7rem;
            ">Kết quả phân cụm</div>
            <div style="font-size: 0.98rem; font-weight: 700; margin-bottom: 0.3rem;">
                Bất động sản của bạn thuộc nhóm:
            </div>
            <div style="font-size: clamp(1.6rem, 2.4vw, 2rem); font-weight: 900; line-height: 1.2; margin-bottom: 0.5rem;">
                {name}
            </div>
            <div style="font-size: 0.9rem; opacity: 0.8;">
                Mô hình đã so sánh đặc trưng của bài đăng với dữ liệu thị trường hiện có.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
