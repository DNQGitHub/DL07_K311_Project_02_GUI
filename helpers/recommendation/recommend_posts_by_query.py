import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from helpers.load_data import load_recommendation_embeddings, load_recommendation_model
from helpers.data_preprocessing import preprocess_query
from helpers.data_featuring import extract_district, extract_price

def price_sim(price_query, price_series, alpha=1.0):
    if price_query == 0:
        return np.ones(len(price_series))
    
    diff_ratio = np.abs(price_series - price_query) / price_query
    
    sim = np.exp(-alpha * diff_ratio)
    
    return sim

def normalize_score(x):
    if x.max() - x.min() == 0:
        return x * 0
    return (x - x.min()) / (x.max() - x.min())

def recommend_posts_by_query(
    query,
    df,
    top_k=5,
    w_bert=0.6,
    w_price=0.2,
    w_location=0.2
):
    model = load_recommendation_model()
    embeddings = load_recommendation_embeddings()
    
    query_processed = preprocess_query(query)
    
    query_emb = model.encode([query_processed])
    bert_scores = cosine_similarity(query_emb, embeddings)[0]
    
    target_price = extract_price(query_processed)
    price_scores = price_sim(target_price, df["gia_ban_num"].values)
    
    target_loc = extract_district(query_processed)
    if target_loc:
        location_scores = (df["quan"] == target_loc).astype(int).values
    else:
        location_scores = np.zeros(len(df))

    bert_norm = normalize_score(bert_scores)
    price_norm = normalize_score(price_scores)
    loc_norm = normalize_score(location_scores)
    
    final_score = (
        w_bert * bert_norm +
        w_price * price_norm +
        w_location * loc_norm
    )
    
    top_idx = np.argsort(final_score)[-top_k:][::-1]
    
    return df.iloc[top_idx]