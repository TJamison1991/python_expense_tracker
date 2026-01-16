# expense_tracker/analytics.py

def get_monthly_total(expenses,month):
    return sum(
        expense["amount"]
        for expense in expenses
        if expense["date"].startswith(month)
    )

def get_category_totals(expenses):
    totals = {}

    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense['amount']
    
    return totals