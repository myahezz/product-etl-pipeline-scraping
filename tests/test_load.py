import pytest
import pandas as pd
import sys
import os
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.load import (
    save_to_csv,
    save_to_postgres,
    save_to_google_sheets
)

# Fixture DataFrame sample
@pytest.fixture
def dummy_dataframe():
    return pd.DataFrame({
        "Title": ["Kaos Putih"],
        "Price": [160000],
        "Rating": [4.9],
        "Colors": [3],
        "Size": ["M"],
        "Gender": ["Unisex"],
        "Timestamp": ["2025-05-27T10:00:00"]
    })

# Test CSV berhasil
def test_csv_save_success(tmp_path, dummy_dataframe):
    target_file = tmp_path / "hasil_test.csv"
    save_to_csv(dummy_dataframe, filename=str(target_file))
    assert target_file.exists()
    df_loaded = pd.read_csv(target_file)
    assert not df_loaded.empty
    assert list(df_loaded.columns) == list(dummy_dataframe.columns)

# Test CSV gagal
@patch("pandas.DataFrame.to_csv", side_effect=Exception("Permission denied"))
def test_csv_save_error(mock_csv, capsys, dummy_dataframe):
    save_to_csv(dummy_dataframe, filename="tidak_valid.csv")
    captured = capsys.readouterr()
    assert "Gagal simpan CSV" in captured.out

# Test PostgreSQL berhasil
@patch("utils.load.create_engine")
def test_postgres_save_success(mock_engine_creator, dummy_dataframe):
    dummy_engine = MagicMock()
    mock_engine_creator.return_value = dummy_engine
    dummy_dataframe.to_sql = MagicMock()
    save_to_postgres(dummy_dataframe)
    dummy_dataframe.to_sql.assert_called_once()

# Test PostgreSQL gagal
@patch("utils.load.create_engine", side_effect=Exception("Tidak bisa koneksi"))
def test_postgres_save_error(mock_engine, dummy_dataframe, capsys):
    save_to_postgres(dummy_dataframe)
    captured = capsys.readouterr()
    assert "PostgreSQL Error" in captured.out

# Test Google Sheets berhasil
@patch("utils.load.Credentials.from_service_account_file")
@patch("utils.load.build")
def test_sheets_save_success(mock_build, mock_creds, dummy_dataframe):
    mock_service = MagicMock()
    mock_spreadsheet = MagicMock()
    mock_values = MagicMock()

    mock_service.spreadsheets.return_value = mock_spreadsheet
    mock_spreadsheet.values.return_value = mock_values
    mock_values.clear.return_value.execute.return_value = None
    mock_values.update.return_value.execute.return_value = None

    mock_build.return_value = mock_service

    save_to_google_sheets(dummy_dataframe)
    assert mock_values.clear.called
    assert mock_values.update.called

# Test Google Sheets gagal
@patch("utils.load.Credentials.from_service_account_file", side_effect=Exception("Berkas tidak valid"))
def test_sheets_save_error(mock_creds, dummy_dataframe, capsys):
    save_to_google_sheets(dummy_dataframe)
    captured = capsys.readouterr()
    assert "Sheets Error" in captured.out