import streamlit as st
import pandas as pd
from datetime import datetime
from dateutil import relativedelta

def display(bieu_do_gia):
    if not bieu_do_gia or bieu_do_gia == "[]":
        st.write("Không có dữ liệu biểu đồ giá bán theo thời gian.")
        return
    
    
    gia = bieu_do_gia.replace("[", "").replace("]", "").split(",")
    gia = [float(g.strip()) for g in gia]
    
    time = [datetime.now() - relativedelta.relativedelta(months=len(gia) - i) for i in range(len(gia))]

    bieu_do_gia_df = pd.DataFrame({
        "price": gia,
        "month": time
    })
        
    st.line_chart(bieu_do_gia_df, x="month", y="price")