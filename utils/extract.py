import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
from time import sleep

HEADERS = {"User-Agent": "Mozilla/5.0"}

def fetch_html(url):
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.content
    except Exception as err:
        print(f"Gagal mengakses {url}: {err}")
        return None

def extract_value(elements, keyword, pattern, default="N/A"):
    for el in elements:
        if el and keyword in el.get_text():
            match = re.search(pattern, el.get_text())
            if match:
                return match.group(1).strip()
    return default

def parse_card(product):
    try:
        title = product.select_one(".product-details h3.product-title")
        title = title.get_text(strip=True) if title else "Tanpa Nama"

        price_section = product.find("div", class_="price-container")
        price = price_section.get_text(strip=True) if price_section else "Tidak Ada Harga"

        paragraphs = product.find_all("p")
        rating = extract_value(paragraphs, "Rating", r"Rating:\s*⭐\s*(\d+(?:\.\d+)?)", "0")
        colors = extract_value(paragraphs, "Colors", r"(\d+)\s*Colors", "0")
        size = extract_value(paragraphs, "Size", r"Size:\s*(\w+)", "Unknown")
        gender = extract_value(paragraphs, "Gender", r"Gender:\s*(\w+)", "Unknown")

        return {
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Colors": colors,
            "Size": size,
            "Gender": gender,
            "Timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        print(f"Gagal parsing produk: {e}")
        return None

def extract_data(page_count=50, delay=1):
    all_items = []
    for i in range(1, page_count + 1):
        page_url = f"https://fashion-studio.dicoding.dev/page{i}" if i > 1 else "https://fashion-studio.dicoding.dev/"
        print(f"Mengambil data dari: {page_url}")
        html = fetch_html(page_url)

        if not html:
            break

        soup = BeautifulSoup(html, "html.parser")
        cards = soup.find_all("div", class_="collection-card")

        for card in cards:
            data = parse_card(card)
            if data:
                all_items.append(data)

        sleep(delay)

    return all_items
