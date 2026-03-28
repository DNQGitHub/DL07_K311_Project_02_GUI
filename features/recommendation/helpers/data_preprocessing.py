import re
from features.recommendation.helpers.load_data import load_recommendation_stopwords

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
    stopwords = load_recommendation_stopwords()
    
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

def preprocess_query(query):
    query = query.lower()
    query = preserve_location(query)
    query = clean_text(query)
    query = advanced_clean(query)
    return query