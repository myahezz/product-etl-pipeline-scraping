import pandas as pd
from sqlalchemy import create_engine
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

def save_to_csv(df, filename="products.csv"):
    try:
        df.to_csv(filename, index=False)
        print(f"[CSV] Disimpan di {filename}")
    except Exception as e:
        print(f"[CSV Error] Gagal simpan CSV: {e}")

def save_to_postgres(df):
    try:
        engine = create_engine("postgresql+psycopg2://postgres:%40Mahreiz10%3B@localhost:5432/etl_project")
        df.to_sql("products", engine, index=False, if_exists="replace")
        print("[PostgreSQL] Data berhasil dimasukkan ke tabel 'products'.")
    except Exception as e:
        print(f"[PostgreSQL Error] {e}")

def save_to_google_sheets(df):
    try:
        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        creds = Credentials.from_service_account_file("google-sheets-api.json", scopes=scopes)
        service = build('sheets', 'v4', credentials=creds)

        sheet_id = "1BZXGJBtAqCjBzwZa0QxHspX3OXQeWIm8pAbYAga51KQ"
        sheet_range = "Sheet1!A1"

        # Bersihkan dulu
        service.spreadsheets().values().clear(
            spreadsheetId=sheet_id,
            range=sheet_range
        ).execute()

        values = [df.columns.tolist()] + df.astype(str).values.tolist()

        service.spreadsheets().values().update(
            spreadsheetId=sheet_id,
            range=sheet_range,
            valueInputOption="RAW",
            body={"values": values}
        ).execute()
        print("[Google Sheets] Data berhasil diunggah.")

    except Exception as e:
        print(f"[Sheets Error] {e}")
