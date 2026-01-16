# tests/test_storage.py

from pathlib import Path
from storage import load_expenses, save_expenses

def test_save_and_load_expenses(tmp_path):
    test_file = tmp_path / "expenses.json"

    expenses = [
        {"amount": 50, "category": "Bills", "date": "2026-01-01"}
    ]

    save_expenses(expenses, test_file)
    loaded = load_expenses(test_file)

    assert loaded == expenses


def test_load_missing_file(tmp_path):
    test_file = tmp_path / "missing.json"

    expenses = load_expenses(test_file)

    assert expenses == []

def test_load_empty_file(tmp_path):
    test_file = tmp_path / "empty.json"
    test_file.touch()  # creates empty file

    expenses = load_expenses(test_file)

    assert expenses == []
