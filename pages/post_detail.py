
import streamlit as st
import pandas as pd
import components.sidebar as sidebar
import components.post_detail as post_detail
import components.post_price_chart as post_price_chart
import components.post_card_list as post_card_list
from features.recommendation.helpers.load_data import load_recommendation_data, load_recommendation_sim_matrix
from features.recommendation.helpers.recommend_posts_by_idx import recommend_posts_by_idx
from features.clustering.helpers.data_featuring import data_featuring, parse_bieu_do_gia, transform_dien_tich, transform_so_phong_ngu
from features.clustering.helpers.clusterize import clusterize
from features.clustering.helpers.load_data import load_clustering_data

def main():
    st.set_page_config(page_title="Post Detail", layout="wide")
    
    sidebar.display()

    st.markdown(
        """
        <style>
            .pd-section-title {
                font-size: 1.2rem;
                font-weight: 800;
                color: #142e3a;
                margin-top: 1.5rem;
                margin-bottom: 0.8rem;
                padding-bottom: 0.6rem;
                border-bottom: 2px solid rgba(15, 32, 39, 0.1);
            }

            .pd-classification {
                display: flex;
                align-items: center;
                gap: 0.6rem;
                background: #ffffff;
                border: 1px solid rgba(15, 32, 39, 0.1);
                padding: 0.75rem 0.9rem;
                border-radius: 8px;
                margin: 0.75rem 0 1rem 0;
                color: #142e3a;
                box-shadow: none;
            }

            .pd-classification-text {
                font-size: 0.96rem;
                font-weight: 600;
                color: #203a43;
                line-height: 1.35;
            }

            .pd-classification-pill {
                display: inline-block;
                margin-left: 0;
                padding: 0.24rem 0.58rem;
                border-radius: 999px;
                background: linear-gradient(135deg, #ff6b35 0%, #ff4757 100%);
                color: #ffffff;
                font-size: 0.82rem;
                font-weight: 800;
                white-space: nowrap;
            }

            .pd-back-link {
                display: inline-block;
                margin-top: 1rem;
                color: #0f2027;
                text-decoration: none;
                font-weight: 600;
                font-size: 0.95rem;
                transition: all 0.3s ease;
                padding: 0.5rem 0.8rem;
                border-radius: 4px;
            }

            .pd-back-link:hover {
                color: #ff4757;
                background: rgba(255, 107, 53, 0.05);
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    post_id = st.query_params.get("post_id", None)

    if post_id is not None:
        try:
            post_id = int(post_id)
        except ValueError:
            st.markdown('<div style="color: #d32f2f; font-weight: 600; font-size: 1rem; margin: 1rem 0;">❌ ID bài đăng không hợp lệ. Vui lòng quay lại trang danh sách bài đăng.</div>', unsafe_allow_html=True)
            st.markdown("[← Quay lại trang danh sách bài đăng](posts)")
            return
    
    if not post_id and post_id != 0:
        st.markdown('<div style="color: #d32f2f; font-weight: 600; font-size: 1rem; margin: 1rem 0;">❌ Không có ID bài đăng. Vui lòng quay lại trang danh sách bài đăng.</div>', unsafe_allow_html=True)
        st.markdown("[← Quay lại trang danh sách bài đăng](posts)")
        return
    
    df = load_recommendation_data()    
    
    if post_id >= len(df) or post_id < 0:
        st.markdown('<div style="color: #d32f2f; font-weight: 600; font-size: 1rem; margin: 1rem 0;">❌ ID bài đăng không hợp lệ. Vui lòng quay lại trang danh sách bài đăng.</div>', unsafe_allow_html=True)
        st.markdown("[← Quay lại trang danh sách bài đăng](posts)")
        return

    post = df.iloc[post_id]
    post_detail.display(post)
    
    st.markdown('<div class="pd-section-title">🏷️ Phân loại nhà đất</div>', unsafe_allow_html=True)
    post_df = pd.DataFrame([post])
    post_df = data_featuring(post_df)
    our_df = load_clustering_data()
    clusterize_result = clusterize(post_df, our_df)
    st.markdown(
        f'''
        <div class="pd-classification">
            <div class="pd-classification-text">Nhà đất này thuộc phân khúc:</div>
            <span class="pd-classification-pill">{clusterize_result["cluster_name"]}</span>
        </div>
        ''',
        unsafe_allow_html=True,
    )
    
    st.markdown('<div class="pd-section-title">📊 Biểu đồ giá bán theo thời gian</div>', unsafe_allow_html=True)
    post_price_chart.display(post['bieu_do_gia'])
    
    sim_matrix = load_recommendation_sim_matrix()
    recommended_posts = recommend_posts_by_idx(
        idx=post_id, 
        sim_matrix=sim_matrix, 
        df=df, 
        top_k=5, 
    )
    
    st.markdown('<div class="pd-section-title">🔗 Các bài đăng tương tự</div>', unsafe_allow_html=True)
    post_card_list.display(recommended_posts)

    st.markdown('<a href="posts" class="pd-back-link">← Quay lại trang danh sách bài đăng</a>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()