# expense_tracker/storage.py

import json
from pathlib import Path

DATA_FILE = Path("expenses.json")


def load_expenses(file_path=DATA_FILE):
    if not file_path.exists():
        return[]
    
    if file_path.stat().st_size == 0:
        return[]
    
    with open(file_path, "r") as f:
        return json.load(f)
    

def save_expenses(expenses, file_path=DATA_FILE):
    with open(file_path, "w") as f:
        json.dump(expenses, f, indent=4)
