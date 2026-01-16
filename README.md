# Expense Tracker (Python CLI)

A simple command-line expense tracker built in Python.  
This project allows users to record expenses, persist data locally, and view summaries by month and category.

The goal of this project was to practice:
- Python fundamentals
- File I/O
- Clean project structure
- Unit testing with pytest
- Defensive programming and error handling

---

## Features

- Add expenses (amount, category, date, description)
- Persist data locally using JSON
- View all recorded expenses
- Monthly expense summaries
- Category-based expense summaries
- Unit tests using pytest
- Modular, testable codebase

---

## Project Structure

expense_tracker/
├── expense_tracker.py # CLI application
├── storage.py # File I/O logic
├── analytics.py # Business logic
├── expenses.json # Local data storage
├── tests/
│ ├── test_storage.py
│ └── test_analytics.py
├── README.md
└── pyproject.toml # pytest configuration

yaml
Copy code

---

## Requirements

- Python 3.9+
- pytest

Install pytest if needed:

```bash
pip install pytest
How to Run the Application
From the project root:

bash
Copy code
python expense_tracker.py
Follow the on-screen menu to add and view expenses.

Running Tests
Run all tests with:

bash
Copy code
pytest
Run tests with verbose output:

bash
Copy code
pytest -v
Example Expense Format
Expenses are stored as JSON objects in expenses.json:

json
Copy code
{
  "amount": 12.50,
  "category": "Food",
  "description": "Lunch",
  "date": "2026-01-15"
}
Future Improvements
Replace JSON storage with SQLite

Add argument-based CLI (argparse or Typer)

Improve input validation

Add charts and visualizations

Add CI with GitHub Actions

What I Learned
Structuring Python projects for testability

Writing unit tests with pytest

Handling file edge cases safely

Debugging real-world runtime errors

Separating business logic from user input

License
This project is open source and available under the MIT License.

yaml
Copy code

---

# 2️⃣ Pushing the Project to GitHub (Step by Step)

I’ll assume:
- You **do not** have a repo yet
- You’re using the terminal
- You already have Git installed (macOS usually does)

---

## Step 1: Create a GitHub Repository

1. Go to **https://github.com**
2. Click **“New repository”**
3. Repository name:  
expense-tracker

cpp
Copy code
4. Description (optional):  
A Python CLI expense tracker with pytest unit tests

yaml
Copy code
5. Choose **Public**
6. ❌ Do **not** initialize with README (you already have one)
7. Click **Create repository**

Leave this page open — you’ll need it.

---

## Step 2: Initialize Git Locally

In your project directory:

```bash
cd ~/Documents/expense_tracker
git init
Check status:

bash
Copy code
git status