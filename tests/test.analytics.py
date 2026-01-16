# tests/test_analytics.py

from analytics import get_monthly_total, get_category_totals


def sample_expenses():
    return[
        {"amount": 10, "category": "Food", "date": "2026-01-10"},
        {"amount": 20, "category": "Transport", "date": "2026-01-12"},
        {"amount": 5, "category": "Food", "date": "2026-02-01"},
    ]


def test_get_monthly_total():
    expenses = sample_expenses()
    total = get_monthly_total(expenses, "2026-01")
    assert total == 30

def test_get_monthly_total_no_matches():
    expenses = sample_expenses()
    total = get_monthly_total(expenses, "2025-12")
    assert total == 0

def test_get_category_totals():
    expenses = sample_expenses()
    totals = get_category_totals(expenses)

    assert totals["Food"] == 15
    assert totals["Transport"] == 20