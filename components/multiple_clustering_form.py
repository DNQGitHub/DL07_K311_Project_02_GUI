import base64
import streamlit as st
import pandas as pd
from features.clustering.helpers.clusterize import clusterize
from features.clustering.helpers.data_featuring import data_featuring

LABELS = ["Bình dân", "Cao cấp"]

REQUIRED_COLS = [
    "dien_tich",
    "gia_ban",
    "so_phong_ngu",
    "gia_kv_mean",
    "loai_hinh",
    "quan",
    "mo_ta",
]


def render(our_df):
    """Render form đánh giá phân khúc hàng loạt qua upload file CSV."""
    _render_template_section()
    st.divider()
    _render_upload_section(our_df)


def _render_template_section():
    st.markdown(
        '<div style="font-size: 1.14rem; font-weight: 800; color: #142e3a; margin-bottom: 0.6rem;">📋 Tải template CSV</div>',
        unsafe_allow_html=True,
    )
    st.caption("Tải file mẫu để biết đúng cấu trúc cột cần có trước khi upload.")

    template_df = pd.DataFrame(
        {
            "dien_tich": [85.0, 120.5],
            "gia_ban": [2.5, 4.8],
            "so_phong_ngu": [2.0, 3.0],
            "gia_kv_mean": [2.8, 5.0],
            "loai_hinh": ["Chung cư", "Nhà phố"],
            "quan": ["Quận 1", "Quận 3"],
            "mo_ta": [
                "Căn hộ 2 phòng ngủ, vị trí trung tâm, gần metro",
                "Nhà phố 3 phòng ngủ, có sân vườn, đường trước nhà rộng",
            ],
        }
    )

    col_btn, _ = st.columns([1, 2])
    with col_btn:
        st.download_button(
            label="⬇️ Tải CSV template",
            data=template_df.to_csv(index=False),
            file_name="template_clustering.csv",
            mime="text/csv",
            use_container_width=True,
        )

    st.markdown(
        '<div style="font-size: 0.88rem; font-weight: 700; color: #142e3a; margin-top: 0.8rem; margin-bottom: 0.3rem;">Xem trước template:</div>',
        unsafe_allow_html=True,
    )
    st.dataframe(template_df, use_container_width=True, hide_index=True)


def _render_upload_section(our_df):
    if "batch_processing" not in st.session_state:
        st.session_state.batch_processing = False
    if "batch_result" not in st.session_state:
        st.session_state.batch_result = None

    st.markdown(
        '<div style="font-size: 1.14rem; font-weight: 800; color: #142e3a; margin-bottom: 0.6rem;">📤 Upload file CSV</div>',
        unsafe_allow_html=True,
    )

    uploaded_file = st.file_uploader(
        "Chọn file CSV chứa thông tin các căn nhà",
        type="csv",
        key="multiple_clustering_file",
    )

    if uploaded_file is None:
        st.session_state.batch_result = None
        return

    try:
        batch_df = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"❌ Không đọc được file: {e}")
        return

    st.markdown(
        '<div style="font-size: 0.88rem; font-weight: 700; color: #142e3a; margin-top: 0.8rem; margin-bottom: 0.3rem;">Xem trước dữ liệu:</div>',
        unsafe_allow_html=True,
    )
    st.dataframe(batch_df.head(), use_container_width=True)

    missing_cols = [c for c in REQUIRED_COLS if c not in batch_df.columns]
    if missing_cols:
        st.error(f"❌ File CSV thiếu cột: **{', '.join(missing_cols)}**")
        return

    btn_label = "⏳ Đang xử lý..." if st.session_state.batch_processing else "Đánh Giá Hàng Loạt"
    clicked = st.button(
        btn_label,
        use_container_width=True,
        key="multiple_clustering_btn",
        type="primary",
        disabled=st.session_state.batch_processing,
    )

    if clicked and not st.session_state.batch_processing:
        st.session_state.batch_processing = True
        st.session_state.batch_df_cache = batch_df
        st.session_state.batch_result = None
        st.rerun()

    if st.session_state.batch_processing:
        try:
            cached_df = st.session_state.batch_df_cache
            batch_copy = cached_df[REQUIRED_COLS].copy()
            batch_copy["full_text"] = batch_copy["mo_ta"]
            batch_featured = data_featuring(batch_copy)

            cluster_labels = []
            for _, row in batch_featured.iterrows():
                result = clusterize(pd.DataFrame([row]), our_df)
                cluster_labels.append(result["cluster_label"])

            result_df_full = cached_df.copy()
            result_df_full["cluster_label"] = cluster_labels
            result_df_full["cluster_name"] = [LABELS[int(l)] for l in cluster_labels]
            st.session_state.batch_result = result_df_full
        except Exception as e:
            st.error(f"❌ Lỗi khi xử lý: {e}")
        st.session_state.batch_processing = False
        st.rerun()

    if st.session_state.batch_result is not None:
        result_df_full = st.session_state.batch_result
        st.success(f"✅ Hoàn thành! Đã đánh giá **{len(result_df_full)}** bất động sản.")

        st.markdown(
            '<div style="font-size: 0.88rem; font-weight: 700; color: #142e3a; margin-top: 0.8rem; margin-bottom: 0.3rem;">📊 Kết quả đánh giá:</div>',
            unsafe_allow_html=True,
        )

        # Build HTML table with colored badge for cluster_name
        tag_styles = {
            "Bình dân": "background:#e9fff4; color:#1e6b3e; border:1px solid rgba(15,160,100,0.3);",
            "Cao cấp":  "background:#ebf4ff; color:#1a4a8a; border:1px solid rgba(15,80,200,0.3);",
        }
        col_labels = {
            "dien_tich": "Diện tích (m²)",
            "gia_ban": "Giá bán (tỷ)",
            "so_phong_ngu": "Số phòng ngủ",
            "gia_kv_mean": "Giá TB khu vực",
            "loai_hinh": "Loại hình",
            "quan": "Quận",
            "mo_ta": "Mô tả",
            "cluster_name": "Phân khúc",
        }
        display_cols = [c for c in REQUIRED_COLS if c in result_df_full.columns] + ["cluster_name"]

        header_cells = "".join(
            f'<th style="padding:0.5rem 0.75rem; text-align:left; font-size:0.82rem; '
            f'font-weight:700; color:#142e3a; border-bottom:2px solid #e0e7ef; white-space:nowrap;">{col_labels.get(c, c)}</th>'
            for c in display_cols
        )

        rows_html = ""
        for _, row in result_df_full.iterrows():
            cells = ""
            for c in display_cols:
                val = row[c]
                if c == "cluster_name":
                    style = tag_styles.get(str(val), "background:#f3f3f3; color:#333;")
                    cell = (
                        f'<span style="{style} border-radius:999px; padding:0.18rem 0.65rem; '
                        f'font-size:0.8rem; font-weight:700; display:inline-block;">{val}</span>'
                    )
                elif c == "mo_ta":
                    cell = f'<span style="font-size:0.85rem; color:#2d3a45;">{val}</span>'
                else:
                    cell = f'<span style="font-size:0.85rem; color:#2d3a45;">{val}</span>'
                cells += f'<td style="padding:0.5rem 0.75rem; border-bottom:1px solid #edf2f7; vertical-align:top;">{cell}</td>'
            rows_html += f"<tr>{cells}</tr>"

        table_html = f"""
        <div style="overflow-x:auto; border-radius:10px; border:1px solid #e0e7ef; margin-top:0.5rem;">
            <table style="width:100%; border-collapse:collapse; background:#fff;">
                <thead><tr style="background:#f8fafc;">{header_cells}</tr></thead>
                <tbody>{rows_html}</tbody>
            </table>
        </div>
        """
        st.markdown(table_html, unsafe_allow_html=True)

        csv_data = result_df_full[["mo_ta", "cluster_name"]].to_csv(index=False)
        b64 = base64.b64encode(csv_data.encode("utf-8")).decode()
        st.markdown(
            f'<a href="data:text/csv;base64,{b64}" download="clustering_result.csv" '
            f'style="font-size: 0.95rem; color: #1a56db; text-decoration: underline; '
            f'font-weight: 600; cursor: pointer;">⬇️ Tải kết quả (CSV)</a>',
            unsafe_allow_html=True,
        )
