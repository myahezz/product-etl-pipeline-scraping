# 🚀 Product Data ETL Pipeline (Web Scraping → Data Storage → Analytics)

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Status](https://img.shields.io/badge/status-active-success)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

An end-to-end **ETL pipeline** built with Python to collect product data via **web scraping**, perform **data cleaning & transformation**, and load the results into multiple destinations (**CSV, PostgreSQL, and Google Sheets**).

> Mirrors a real-world Data Engineering workflow: **ingestion → processing → storage → validation**

---

## ✨ Highlights

- ⚡ Modular ETL architecture (Extract–Transform–Load)
- 🔍 Scalable web scraping (multi-page support)
- 🧹 Robust data cleaning & preprocessing
- 🗄️ Multi-destination loading (CSV, PostgreSQL, Google Sheets)
- 🧪 Unit testing with pytest
- 📊 Test coverage reporting
- 🧱 Clean and maintainable structure (separation of concerns)

---

## 🧠 Use Cases

- Data ingestion from websites / marketplaces
- Data preprocessing before analytics / machine learning
- Lightweight pipelines for reporting / dashboards

---

## 🏗️ System Architecture

```
                ┌──────────────────────┐
                │     Data Source      │
                │   (Website / API)   │
                └──────────┬──────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │       EXTRACT        │
                │   extract_data()     │
                │  (Web Scraping)      │
                └──────────┬──────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │      TRANSFORM       │
                │ clean_dataframe()    │
                │ Data Cleaning & Prep │
                └──────────┬──────────┘
                           │
                           ▼
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
┌──────────────┐  ┌──────────────┐  ┌────────────────┐
│     CSV      │  │ PostgreSQL   │  │ Google Sheets  │
│ (Data Lake)  │  │ (Data Store) │  │ (Analytics)    │
└──────────────┘  └──────────────┘  └────────────────┘
```

---

## 📁 Project Structure

```
.
├── main.py                     # Pipeline entry point
├── utils/
│   ├── extract.py             # Web scraping (Extract)
│   ├── transform.py           # Data cleaning (Transform)
│   └── load.py                # Data loading (Load)
├── tests/                     # Unit tests (pytest)
├── data/
│   └── products.csv           # Sample output
├── google-sheets-api.json     # Google Sheets credential (excluded)
├── requirements.txt           # Dependencies
├── submission.txt             # Submission metadata
└── README.md
```

---

## ⚡ Quick Start

```bash
git clone https://github.com/username/product-etl-pipeline.git
cd product-etl-pipeline
pip install -r requirements.txt
python main.py
```

---

## 🔐 Environment Setup

### Google Sheets

1. Create credentials via Google Cloud Console
2. Download JSON key
3. Save as:

```bash
google-sheets-api.json
```

> ⚠️ Do **NOT** commit this file. Add it to `.gitignore`.

---

### (Optional) Environment Variables

Create `.env` file:

```bash
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=your_db
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
```

---

## ▶️ Pipeline Steps

1. **Extract** → scrape product data
2. **Transform** → clean, normalize, validate
3. **Load** → store into:
   - CSV
   - PostgreSQL
   - Google Sheets

---

## 🧪 Testing & Quality

```bash
pytest tests
```

Coverage:

```bash
coverage run -m pytest tests
coverage report -m
```

✔ Ensures pipeline reliability
✔ Validates data processing logic

---

## 📊 Sample Output

**Example (cleaned data):**

| product_name | price | rating |
| ------------ | ----: | -----: |
| Product A    |   100 |    4.5 |
| Product B    |   200 |    4.8 |

**Artifacts:**

- CSV file (`data/products.csv`)
- PostgreSQL table
- Google Sheets (live):

👉 https://docs.google.com/spreadsheets/d/1BZXGJBtAqCjBzwZa0QxHspX3OXQeWIm8pAbYAga51KQ

## 🛠️ Tech Stack

- Python
- Pandas
- PostgreSQL
- Google Sheets API
- Pytest
- Coverage

---

## ⚠️ Limitations

- No workflow orchestration yet (Airflow / Prefect)
- Logging can be improved with structured logging
- Full load only (no incremental ingestion)

---

## 🚀 Roadmap

- 🔄 Workflow orchestration (Apache Airflow)
- 🐳 Docker containerization
- 📜 Structured logging (logging module / ELK)
- ⚡ Incremental data ingestion
- ☁️ Cloud deployment (GCP / AWS)
- 📊 BI / dashboard integration

---

## 🎯 Why This Project Matters

This project demonstrates real-world data engineering capabilities:

- **Data Ingestion** → Web scraping
- **Data Transformation** → Cleaning & structuring
- **Data Loading** → Multi-target storage
- **Data Validation** → Testing & QA
- **System Design** → Modular and maintainable ETL

💼 Relevant for roles:

- Data Engineer
- AI Engineer
- Backend Engineer (Data-focused)

---

## 👨‍💻 Author

* **Nama**      : Wildan Septian
* **GitHub**    : [myahezz](https://github.com/myahezz)
* **LinkedIn**  : [wildanseptian](https://www.linkedin.com/in/wildanseptian)
* **Instagram** : [myahezzz](https://www.instagram.com/myahezzz/)

---

## 📄 License

MIT License
