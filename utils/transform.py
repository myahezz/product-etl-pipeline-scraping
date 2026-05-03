import pandas as pd
import re

def format_price(value):
    if not isinstance(value, str):
        return None
    value = value.lower().strip()

    try:
        if "$" in value:
            number = float(re.sub(r"[^\d.]", "", value))
            return number * 16000
        elif "rp" in value:
            number = float(re.sub(r"[^\d.]", "", value.replace("rp", "")))
            return number
    except:
        return None
    return None

def format_rating(val):
    try:
        return float(val) if 0 <= float(val) <= 5 else None
    except:
        return None

def parse_color_count(text):
    try:
        match = re.search(r"-?\d+", str(text))
        count = int(match.group()) if match else 0
        return count if count >= 0 else 0
    except:
        return 0


def clean_dataframe(df):
    df = df.copy()
    df['Price'] = df['Price'].apply(format_price)
    df['Rating'] = df['Rating'].apply(format_rating)
    df['Colors'] = df['Colors'].apply(parse_color_count)

    df = df.dropna(subset=['Price', 'Rating'])
    df = df[df['Price'] > 0]
    df = df.drop_duplicates()
    df = df[df['Title'] != 'Unknown Product']
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    return df