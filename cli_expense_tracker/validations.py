from cli_expense_tracker.exceptions import InvalidExpenseDataError, FutureDateExpenseDateError
from datetime import datetime, date

def validate_amount(amount):
    if amount <= 0:
        raise InvalidExpenseDataError("Amount must be positive!!!")
    return amount

def validate_category(category):
    if not category or not category.strip():
        raise InvalidExpenseDataError("Categoy must not be empty")
    return category.strip()

def validate_date(date_str):
    try:
        parsed_date = datetime.strptime(date_str,"%Y-%m-%d").date()
    except ValueError:
        raise InvalidExpenseDataError(f"Invalid date: {date_str}. Expected format YYYY-MM-DD")
    if parsed_date > date.today():
        raise FutureDateExpenseDateError(f"Time Machine hasn't been invented yet!!! \n {date_str} is in future.")
    return date_str