# expense_tracker/expense_tracker.py

from datetime import datetime
from storage import load_expenses, save_expenses
from analytics import get_monthly_total, get_category_totals


def show_menu():
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View expenses")
    print("3. Monthly summary")
    print("4. Category summary")
    print("5. Exit")


def add_expense(expenses):
    try:
        amount = float(input("Amount: "))
        category = input("Category: ").strip()
        description = input("Description: ").strip()
        date = input("Date (YYYY-MM-DD) or leave blank: ")

        if not date:
            date = datetime.today().strftime("%Y-%m-%d")

        expenses.append({
            "amount": amount,
            "category": category,
            "description": description,
            "date": date
        })
        
        save_expenses(expenses)
        print("Expense added!")
    
    except ValueError:
        print("Invalid input")


def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return
    
    for i, e in enumerate(expenses, 1):
        print(
            f"{i}. {e['date']} | {e['category']} | "
            f"${e['amount']:.2f} | {e['description']}"
        )


def monthly_summary(expenses):
    month = input("Enter month (YYYY-MM): ")
    total = get_monthly_total(expenses, month)
    print(f"Total for {month}: ${total:.2f}")


def category_summary(expenses):
    totals = get_category_totals(expenses)
    for category, total in totals.items():
        print(f"{category}: ${total:.2f}")


def main():
    expenses = load_expenses()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            monthly_summary(expenses)
        elif choice == "4":
            category_summary(expenses)
        elif choice == "5":
            break
        else:
            print("Invalid option")


if __name__=="__main__":
    main()