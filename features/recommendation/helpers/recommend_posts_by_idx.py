import numpy as np

def price_sim(i, j, df):
    return 1 - abs(df.loc[i,"gia_scaled"] - df.loc[j,"gia_scaled"])

def location_sim(i, j, df):
    return 1 if df.loc[i, "quan"] == df.loc[j, "quan"] else 0

def collect_scores(idx, sim_matrix, df, w_text=0.6, w_price=0.2, w_loc=0.2):
    sims_text = sim_matrix[idx]

    scores = []

    for j in range(len(df)):
        sim_price = price_sim(idx, j, df)
        sim_loc = location_sim(idx, j, df)

        score = (
            w_text * sims_text[j] +
            w_price * sim_price +
            w_loc * sim_loc
        )
        scores.append(score)
    
    return np.array(scores)

def recommend_posts_by_idx(
    idx,
    sim_matrix,
    df,
    top_k=5,
    w_text=0.6,
    w_price=0.2,
    w_loc=0.2
):
    scores = collect_scores(idx, sim_matrix, df, w_text, w_price, w_loc)
    top_idx = np.argsort(scores)[::-1][1:top_k + 1]
    recommended_posts = df.iloc[top_idx]
    
    return recommended_posts