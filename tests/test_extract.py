import unittest
from bs4 import BeautifulSoup
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.extract import extract_value, parse_card

class TestExtractionModule(unittest.TestCase):

    def test_extract_value_function(self):
        html = '''
        <p>Rating: ⭐ 4.3</p>
        <p>Colors: 5 Colors</p>
        <p>Size: XL</p>
        <p>Gender: Unisex</p>
        '''
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup.find_all('p')

        self.assertEqual(extract_value(tags, "Rating", r"Rating:\s*⭐\s*(\d+(?:\.\d+)?)"), "4.3")
        self.assertEqual(extract_value(tags, "Colors", r"(\d+)\s*Colors"), "5")
        self.assertEqual(extract_value(tags, "Size", r"Size:\s*(\w+)"), "XL")
        self.assertEqual(extract_value(tags, "Gender", r"Gender:\s*(\w+)"), "Unisex")
        self.assertEqual(extract_value(tags, "Brand", r"Brand:\s*(\w+)", "Default"), "Default")

    def test_parse_card_function(self):
        html = '''
        <div class="collection-card">
            <div class="product-details">
                <h3 class="product-title">Kaos Merah</h3>
            </div>
            <div class="price-container">$10</div>
            <p>Rating: ⭐ 4.8</p>
            <p>Colors: 1 Colors</p>
            <p>Size: S</p>
            <p>Gender: Male</p>
        </div>
        '''
        soup = BeautifulSoup(html, "html.parser")
        card = soup.find("div", class_="collection-card")
        result = parse_card(card)

        self.assertEqual(result["Title"], "Kaos Merah")
        self.assertEqual(result["Price"], "$10")
        self.assertEqual(result["Rating"], "4.8")
        self.assertEqual(result["Colors"], "1")
        self.assertEqual(result["Size"], "S")
        self.assertEqual(result["Gender"], "Male")
        self.assertIn("Timestamp", result)

if __name__ == '__main__':
    unittest.main()