# tests/test_storage.py

from pathlib import Path
from storage import load_expenses, init_db, add_expense

def test_add_and_load_expense(tmp_path):
    db = tmp_path / "test.db"
    init_db(db)

    add_expense(
        {
            "amount": 100,
            "category": "Food",
            "description": "Lunch",
            "date": "2026-01-10",
        },
        db,
    )

    expenses = load_expenses(db)

    assert len(expenses) == 1
    assert expenses[0]["amount"] == 100
    assert expenses[0]["category"] == "Food"
