from datetime import datetime
from storage import init_db, load_expenses, add_expense
from analytics import get_monthly_total, get_category_totals


def show_menu():
    print("\nExpense Tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Monthly summary")
    print("4. Category summary")
    print("5. Exit")


def add_expense_cli():
    try:
        amount = float(input("Amount: "))
        category = input("Category: ").strip()
        description = input("Description: ").strip()
        date = input("Date (YYYY-MM-DD) or leave blank: ")

        if not date:
            date = datetime.today().strftime("%Y-%m-%d")

        add_expense({
            "amount": amount,
            "category": category,
            "description": description,
            "date": date
        })

        print("✅ Expense added")

    except ValueError:
        print("❌ Invalid input")


def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    for e in expenses:
        print(
            f"{e['date']} | {e['category']} | "
            f"${e['amount']:.2f} | {e['description']}"
        )


def main():
    init_db()

    while True:
        expenses = load_expenses()
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense_cli()
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            month = input("Month (YYYY-MM): ")
            total = get_monthly_total(expenses, month)
            print(f"Total: ${total:.2f}")
        elif choice == "4":
            totals = get_category_totals(expenses)
            for cat, total in totals.items():
                print(f"{cat}: ${total:.2f}")
        elif choice == "5":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
