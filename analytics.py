# expense_tracker/analytics.py

def get_monthly_total(expenses,month):
    return sum(
        e["amount"]
        for e in expenses
        if e["date"].startswith(month)
    )

def get_category_totals(expenses):
    totals = {}

    for e in expenses:
        category = e["category"]
        totals[category] = totals.get(category, 0) + e['amount']
    
    return totals