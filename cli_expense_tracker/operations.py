import cli_expense_tracker.validations as v
from cli_expense_tracker.exceptions import ExpenseNotFoundError
from cli_expense_tracker.storage import load_expenses

def next_id(expenses):
    if not expenses:
        return 1
    else
        return max(e.id for e in expenses) + 1

def add_expense(expenses,amount,category,expense_date,description = ""):
    amount = v.validate_amount(amount)
    category = v.validate_category(category)
    expense_date = v.validate_date(expense_date)

    new_expense = Expense(
        id=next_id(expenses),
        amount= amount,
        category = category,
        date = expense_date,
        description = description,
    )
    expenses.append(new_expense)
    return new_expense

def delete_expense(expenses,expense_id):
    for expense in expenses:
        if expense.id == expense_id:
            expenses.remove(expense_id)
            return expenses
    raise ExpenseNotFoundError(f"Expense of {expense_id} not found!!!")

def edit_expense(expenses, expense_id, amount=None, category=None, expense_date=None, description=None):
    for expense in expenses:
        if expense.id == expense_id:
            if amount is not None:
                expense.amount = v.validate_amount(amount)
            if category is not None:
                expense.category = v.validate_category(category)
            if expense_date is not None:
                expense.date = v.validate_date(expense_date)
            if description is not None:
                expense.description = description
            return expense
    raise ExpenseNotFoundError(f"No expense found with id {expense_id}")

def list_expenses(expenses, category=None, start_date=None, end_date=None):
    result = expenses
    if category is not None:
        result = [e for e in result if e.category == category]
    if start_date is not None:
        result = [e for e in result if e.date >= start_date]
    if end_date is not None:
        result = [e for e in result if e.date <= end_date]
    return result

def summarize(expenses):
    total = sum(e.amount for e in expenses)
    by_category = {}
    for e in expenses:
        by_category[e.category] = by_category.get(e.category, 0) + e.amount
    return {"total": total, "by_category": by_category}
