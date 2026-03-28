import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from helpers.load_data import load_clustering_model


def clusterize(user_df, our_df):
    core_features = [
        "dien_tich", "gia_ban", "so_phong_ngu", "gia_kv_mean",
        "is_mat_tien", "has_thang_may", "tien_nghi_score"
    ]
            
    core_features = [f for f in core_features if f in our_df.columns]
    core_features = [f for f in core_features if f in user_df.columns]

    cat_enc_features = [c + "_enc" for c in ["loai_hinh", "quan"] if c + "_enc" in user_df.columns]

    selected_features = core_features + cat_enc_features

    user_df_optimized = user_df[selected_features]
    our_df_optimized = our_df[selected_features]
    
    df_optimized = pd.concat([user_df_optimized, our_df_optimized], ignore_index=True)
    
    for col in ["gia_ban", "dien_tich"]:
        if col in df_optimized.columns:
            df_optimized[col] = np.log1p(df_optimized[col])  # log(1+x) để handle 0

    # Scale
    scaler_opt = StandardScaler()
    x_optimized = scaler_opt.fit_transform(df_optimized.dropna())            
    
    model = load_clustering_model() 
    cluster_label = model.fit_predict(x_optimized)
    df_optimized["segment"] = cluster_label
    
    print(user_df_optimized.head(1))
    print(df_optimized[df_optimized["segment"] == 1].head(1))
    
    labels = ["Bình dân", "Cao cấp", "Siêu sang", "Ultra Premium", "Ultra"]
    
    return { "cluster_label": cluster_label[0], "cluster_name": labels[cluster_label[0]] }