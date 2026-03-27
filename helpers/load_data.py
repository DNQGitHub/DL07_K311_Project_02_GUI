import pandas as pd

def load_data():
    df = pd.read_parquet("data/dataset_cleaned.parquet")
    return df