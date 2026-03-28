import re

def get_location_tokens():
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
    
    locations = [loc.replace(" ", "_") for loc in locations]
    
    return locations

def extract_price(query):
    match = re.search(r"(\d+(\.\d+)?)\s*tỷ", query)
    if match:
        return float(match.group(1))
    return None

def extract_district(query):
    locations = get_location_tokens()

    if query is None:
        return "unknown"
   
    for loc in locations:
        if loc in  query:
            return loc

    return "unknown"
