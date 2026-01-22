Expense Tracker (Python, SQLite, pytest)

A simple command-line expense tracker built with Python, featuring persistent storage using SQLite and a clean, testable architecture with pytest.

This project demonstrates real-world Python practices such as separation of concerns, database-backed storage, and automated testing.

✨ Features

Add and view expenses from the command line

Monthly expense summaries

Category-based summaries

Persistent storage using SQLite

Fully tested business logic with pytest

Clean, beginner-friendly architecture

🛠️ Tech Stack

Python 3

SQLite (via Python standard library sqlite3)

pytest for testing

SQLite is included with Python — no external database setup required.

📁 Project Structure
expense_tracker/
│
├── expense_tracker.py      # CLI application
├── storage.py              # SQLite persistence layer
├── analytics.py            # Business logic
│
├── tests/
│   ├── test_storage.py
│   └── test_analytics.py
│
├── pyproject.toml
├── .gitignore
└── README.md

🚀 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker

2️⃣ (Optional) Create a Virtual Environment
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install pytest


No database installation is required — SQLite is built into Python.

▶️ Running the Application

From the project root:

python expense_tracker.py


Follow the on-screen menu to add and view expenses.

🧪 Running the Tests
pytest


Or with verbose output:

pytest -v


Tests use temporary SQLite databases and do not affect real data.

🗄️ Storage Details

Expenses are stored in a local SQLite database (expenses.db)

The database file is ignored by Git

Tables are created automatically on first run

🧠 Design Notes

Storage layer handles all database interactions

Analytics layer contains pure business logic

CLI layer remains thin and user-focused

Architecture is designed for easy refactoring and extension

🔮 Possible Future Improvements

Edit and delete expenses

SQLAlchemy ORM

REST API with FastAPI

GitHub Actions CI

Code coverage reporting

📌 Why This Project?

This project was built to practice and demonstrate:

Python fundamentals

SQLite database integration

Test-driven, modular design

Professional project structure suitable for a portfolio