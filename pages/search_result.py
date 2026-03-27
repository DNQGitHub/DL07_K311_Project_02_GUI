from helpers.load_data import load_data
import streamlit as st
import components.sidebar as sidebar
import re
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import re
from sklearn.preprocessing import MinMaxScaler


def extract_price(query):
    match = re.search(r"(\d+(\.\d+)?)\s*tỷ", query)
    if match:
        return float(match.group(1))
    return None

def extract_district(query):
    match = re.search(r"Quận\s*([\w\s]+)", query)
    if match:
        return match.group(1).strip().lower().replace(" ", "_")
    return "unknown"

def preserve_location(text):
    locations = [
        "tân sơn nhất",
        "gia định",
        "bình tân",
        "thủ đức",
        "bình thạnh",
        "gò vấp",
        "phú nhuận",
        "tân bình",
        "tân phú",
        "bình chánh",
        "cần giờ",
        "củ chi",
        "hóc môn",
        "nhà bè"
    ]
    
    for quan_so in range(1, 12):
        quan = f"quận {quan_so}"
        locations.append(quan)
    
    for loc in locations:
        text = text.replace(loc, loc.replace(" ", "_"))
    
    return text

def clean_text(text):
    # lowercase
    text = text.lower()
    
    # remove emoji & special characters
    text = re.sub(r"[^\w\s]", " ", text)
    
    # remove numbers (optional, nhưng nên giữ nếu bạn muốn dùng diện tích)
    # text = re.sub(r"\d+", " ", text)
    
    # remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()
    
    return text

def advanced_clean(text):
    STOP_WORD_FILE = 'data/stopwords.txt'
    
    with open(STOP_WORD_FILE, 'r', encoding='utf-8') as file:
        stopwords = file.read()

    stopwords = stopwords.split('\n')
    
    words = text.split()
    
    # remove stopwords
    words = [w for w in words if w not in stopwords]
    
    # remove duplicate words (giữ thứ tự)
    seen = set()
    new_words = []
    for w in words:
        if w not in seen:
            new_words.append(w)
            seen.add(w)
    
    return " ".join(new_words)

def preprocess_query(text):
    text = text.lower()
    
    test = preserve_location(text)
    text = clean_text(test)
    text = advanced_clean(text)

    return text

def price_sim(price_query, price_series, alpha=1.0):
    print("Calculating price similarity...")
    print("Price query:", price_query, type(price_query))
    print("Price series sample:", price_series[:5], type(price_series))
    
    if price_query == 0:
        return np.ones(len(price_series))
    
    diff_ratio = np.abs(price_series - price_query) / price_query
    
    sim = np.exp(-alpha * diff_ratio)
    
    return sim


def recommend_from_query_bert_only(
    query,
    df,
    top_k=5,
    w_bert=0.6,
    w_price=0.2,
    w_location=0.2
):
    model = pickle.load(open('models/recommendation/sentence_transformer_model.pkl', 'rb'))
    embeddings = pickle.load(open('models/recommendation/sentence_transformer_embeddings.pkl', 'rb'))
    
    # ===== 1. preprocess =====
    query_processed = preprocess_query(query)
    
    # ===== 2. BERT (so với embeddings, KHÔNG dùng sim_matrix) =====
    query_emb = model.encode([query_processed])
    bert_scores = cosine_similarity(query_emb, embeddings)[0]
    
    # ===== 3. price =====
    print("=" * 50)
    
    target_price = extract_price(query)
    
    print("Target price extracted from query:", target_price)
    print("Sample prices from dataset:", df["gia_ban_num"].values)
    price_scores = price_sim(target_price, df["gia_ban_num"].values)
    print("Price scores sample:", price_scores[:5])
    # ===== 4. location =====
    query_loc = extract_district(query_processed)
    
    if query_loc:
        location_scores = (df["quan"] == query_loc).astype(int).values
    else:
        location_scores = np.zeros(len(df))
    
    # ===== 5. normalize =====
    def normalize(x):
        if x.max() - x.min() == 0:
            return x * 0
        return (x - x.min()) / (x.max() - x.min())
    
    bert_norm = normalize(bert_scores)
    price_norm = normalize(price_scores)
    loc_norm = normalize(location_scores)
    
    # ===== 6. final score =====
    final_score = (
        w_bert * bert_norm +
        w_price * price_norm +
        w_location * loc_norm
    )
    
    print("BERT scores:", bert_scores[:5])
    print("Price scores:", price_scores[:5])
    print("Location scores:", location_scores[:5])
    print("Final scores:", final_score[:5])
    
    # ===== 7. top K =====
    top_idx = np.argsort(final_score)[-top_k:][::-1]
    
    return df.iloc[top_idx]

    

def main():
    sidebar.display()
    df = load_data()
    
    scaler = MinMaxScaler()
    df["gia_scaled"] = scaler.fit_transform(df[["gia_ban_num"]])
    
    query = st.session_state.get("final_query", "")
    st.write("Bạn tìm:", query)
    recommend_result = recommend_from_query_bert_only(query, df)
    
    for index, row in recommend_result.iterrows():
        st.subheader(row["tieu_de"])
        st.write(f"Giá: {row['gia_ban']} - Diện tích: {row['dien_tich']} m2 - Quận: {row['quan'].replace('_', ' ').title()}")
        st.write(row["mo_ta"])
        st.markdown("---")
    
    st.session_state.searched = False

main()