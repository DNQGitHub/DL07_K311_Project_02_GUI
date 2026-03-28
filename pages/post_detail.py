import streamlit as st
import components.sidebar as sidebar
import components.post_detail as post_detail
import components.post_price_chart as post_price_chart
import components.post_card_list as post_card_list
from features.recommendation.helpers.load_data import load_recommendation_data, load_recommendation_sim_matrix
from features.recommendation.helpers.recommend_posts_by_idx import recommend_posts_by_idx

def main():
    sidebar.display()
    
    post_id = st.query_params.get("post_id", None)

    if post_id is not None:
        try:
            post_id = int(post_id)
        except ValueError:
            st.write("ID bài đăng không hợp lệ. Vui lòng quay lại trang danh sách bài đăng.")
            st.markdown("[Quay lại trang danh sách bài đăng](posts)")
            return
    
    if not post_id and post_id != 0:
        st.write("Không có ID bài đăng. Vui lòng quay lại trang danh sách bài đăng.")
        st.markdown("[Quay lại trang danh sách bài đăng](posts)")
        return
    
    df = load_recommendation_data()    
    
    if post_id >= len(df) or post_id < 0:
        st.write("ID bài đăng không hợp lệ. Vui lòng quay lại trang danh sách bài đăng.")
        st.markdown("[Quay lại trang danh sách bài đăng](posts)")
        return

    post = df.iloc[post_id]

    post_detail.display(post)
    
    st.write("### Biểu đồ giá bán theo thời gian")
    post_price_chart.display(post['bieu_do_gia'])
    
    sim_matrix = load_recommendation_sim_matrix()
    recommended_posts = recommend_posts_by_idx(
        idx=post_id, 
        sim_matrix=sim_matrix, 
        df=df, 
        top_k=5, 
    )
    
    st.write("### Các bài đăng tương tự")
    post_card_list.display(recommended_posts)

    st.markdown("---")
    st.markdown("[Quay lại trang danh sách bài đăng](posts)")

main()