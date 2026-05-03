import pandas as pd
from utils.extract import extract_data
from utils.transform import clean_dataframe
from utils.load import save_to_csv, save_to_postgres, save_to_google_sheets

def main():
    try:
        print("📥 Mulai proses pengambilan data produk...")
        raw_data = extract_data(page_count=50)

        if not raw_data:
            print("Data tidak ditemukan. ETL dibatalkan.")
            return

        df_raw = pd.DataFrame(raw_data)
        print(f"Ekstraksi selesai. Total item: {len(df_raw)}")

        print("Transformasi data dimulai...")
        df_clean = clean_dataframe(df_raw)
        print(f"Transformasi selesai. Item valid: {len(df_clean)}")

        print("Menyimpan data ke CSV...")
        save_to_csv(df_clean)

        print("Menyimpan ke PostgreSQL...")
        save_to_postgres(df_clean)

        print("Upload ke Google Sheets...")
        save_to_google_sheets(df_clean)

        print("\n=======Informasi Data Setelah Transformasi:=======")
        print(df_clean.info())
        print("\n=======Data Head Setelah Transformasi:=======")
        print(df_clean.head())

        
        print("Proses ETL selesai dengan sukses!")

    except Exception as err:
        print(f"Terjadi error saat proses utama: {err}")

if __name__ == '__main__':
    main()
