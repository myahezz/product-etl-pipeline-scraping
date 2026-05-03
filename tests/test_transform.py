import unittest
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.transform import format_price, format_rating, parse_color_count, clean_dataframe

class TestTransformationModule(unittest.TestCase):

    def test_format_price(self):
        self.assertAlmostEqual(format_price("$1,200.50"), 1200.50 * 16000)
        self.assertAlmostEqual(format_price("Rp 500"), 500.0)
        self.assertIsNone(format_price("-100"))
        self.assertIsNone(format_price("gratis"))
        self.assertIsNone(format_price(None))
        self.assertIsNone(format_price(""))

    def test_format_rating(self):
        self.assertEqual(format_rating("4.5"), 4.5)
        self.assertEqual(format_rating("5"), 5.0)
        self.assertIsNone(format_rating("buruk"))
        self.assertIsNone(format_rating(None))
        self.assertIsNone(format_rating("-1"))
        self.assertIsNone(format_rating("6"))

    def test_parse_color_count(self):
        self.assertEqual(parse_color_count("5 Colors"), 5)
        self.assertEqual(parse_color_count("1"), 1)
        self.assertEqual(parse_color_count("abc"), 0)
        self.assertEqual(parse_color_count("-1"), 0)
        self.assertEqual(parse_color_count(None), 0)

    def test_clean_dataframe_structure(self):
        df = pd.DataFrame({
            "Price": ["Rp 200", "$10", None, "free"],
            "Rating": ["4.0", "3.5", None, "salah"],
            "Colors": ["2 Colors", "3 Colors", "abc", None],
            "Title": ["Produk A", "Produk B", "Produk C", "Produk D"],
            "Timestamp": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04"]
        })
        result = clean_dataframe(df)
        self.assertEqual(len(result), 2)
        self.assertIn("Price", result.columns)
        self.assertIn("Rating", result.columns)
        self.assertIn("Colors", result.columns)
        self.assertIn("Timestamp", result.columns)

    def test_clean_dataframe_values(self):
        df = pd.DataFrame({
            "Price": ["Rp 100", "$2", "invalid", "-100"],
            "Rating": ["5", "3.5", "invalid", None],
            "Colors": ["1", "2 Colors", "abc", None],
            "Title": ["Item 1", "Item 2", "Item 3", "Item 4"],
            "Timestamp": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04"]
        })
        cleaned = clean_dataframe(df)
        self.assertEqual(len(cleaned), 2)
        self.assertTrue(all(cleaned['Price'] > 0))
        self.assertTrue(all(cleaned['Rating'].notnull()))
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(cleaned["Timestamp"]))

if __name__ == '__main__':
    unittest.main()
