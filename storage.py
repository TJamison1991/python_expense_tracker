# expense_tracker/storage.py

import sqlite3
from pathlib import Path

DB_FILE = Path("expenses.db")


def get_connection(db_path=DB_FILE):
    return sqlite3.connect(db_path)

def init_db(db_path=DB_FILE):
    with get_connection(db_path) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                description TEXT,
                date TEXT NOT NULL
            )
        """)

def add_expense(expense, db_path=DB_FILE):
    with get_connection(db_path) as conn:
        conn.execute(
            """
            INSERT INTO expenses (amount, category, description, date)
            VALUES (?,?,?,?)
            """,
            (
                expense["amount"],
                expense["category"],
                expense["description"],
                expense["date"],
            ),
        )


def load_expenses(db_path=DB_FILE):
    with get_connection(db_path) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute("SELECT * FROM expenses").fetchall()
        return [dict(row) for row in rows]

