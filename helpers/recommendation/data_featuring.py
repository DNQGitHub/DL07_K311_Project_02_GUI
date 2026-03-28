import re

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
