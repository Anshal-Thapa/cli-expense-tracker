import pytest
from cli_expense_tracker import validations
from cli_expense_tracker import exceptions
from datetime import date,timedelta

#Amount
def test_validate_amount_accepts_positive_value():
    assert validations.validate_amount(20)==20

def test_validate_amount_rejects_negative_value():
    with pytest.raises(exceptions.InvalidExpenseDataError):
        validations.validate_amount(-5)

def test_validate_amount_rejects_zero_value():
    with pytest.raises(exceptions.InvalidExpenseDataError):
        validations.validate_amount(0)

#Category
def test_validate_category_accepts_normal_string():
    assert validations.validate_category("Food")=="Food"

def test_validate_category_strips_whitespaces():
    assert validations.validate_category("    Food    ")=="Food"

def test_validate_category_rejects_empty_string():
    with pytest.raises(exceptions.InvalidExpenseDataError):
        validations.validate_category("")

def test_validate_category_rejects_whitespaces():
    with pytest.raises(exceptions.InvalidExpenseDataError):
        validations.validate_category("      ")

#Date
def test_validate_date_accepts_past_date():
    assert validations.validate_category("2020-01-12")=="2020-01-12"

def test_validate_date_accepts_today():
    today_str = date.today().isoformat()
    assert validations.validate_date(today_str) == today_str
 
 
def test_validate_date_rejects_bad_format():
    with pytest.raises(exceptions.InvalidExpenseDataError):
        validations.validate_date("15/08/2026")
 
 
def test_validate_date_rejects_impossible_date():
    with pytest.raises(exceptions.InvalidExpenseDataError):
        validations.validate_date("2026-13-45")
 
 
def test_validate_date_rejects_future_date():
    future = (date.today() + timedelta(days=5)).isoformat()
    with pytest.raises(exceptions.FutureDateExpenseDateError):
        validations.validate_date(future)
