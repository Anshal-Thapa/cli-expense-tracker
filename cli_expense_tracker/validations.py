from cli_expense_tracker.exceptions import InvalidExpenceDataError, FutureDateExpenseDateError
from datetime import datetime, date

def validate_amount(amount):
    if amount < 0:
        raise InvalidExpenceDataError("Amount must be positive!!!")
    return amount

def validate_category(category):
    if not category or not category.strip():
        raise InvalidExpenceDataError("Categoy must not be empty")
    return category.strip()

def validate_date(date):
    try:
        parsed_date = strpdate(date,"%Y-%m-%d").date()
    expect ValueError:
        raise InvalidExpenceDataError(f"Invalid date: {date}. Expected format YYYY-MM-DD")
    if parsed_date > date.today():
        raise FutureDateExpenseDateError(f"Time Machine hasn't been invented yet!!! \n {date} is in future.")
    return date