import pytest

from cli_expense_tracker import operations
from cli_expense_tracker.models import Expense
from cli_expense_tracker.exceptions import ExpenseNotFoundError,InvalidExpenseDataError


@pytest.fixture
def sample_expenses():
    return [
        Expense(id=1, amount=20.0, category="food", date="2026-08-01", description="Lunch"),
        Expense(id=3, amount=800.0, category="rent", date="2026-08-15"),
        Expense(id=4, amount=15.0, category="food", date="2026-08-20"),
    ]

def test_next_id_empty_list():
    assert operations.next_id([]) == 1


def test_next_id_with_gap(sample_expenses):
    assert operations.next_id(sample_expenses) == 5


def test_add_expense_appends_and_returns_new_expense(sample_expenses):
    new_expense = operations.add_expense(sample_expenses, 50.0, "transport", "2026-08-25", "Bus")

    assert len(sample_expenses) == 4
    assert new_expense.id == 5
    assert new_expense.amount == 50.0
    assert new_expense.category == "transport"
    assert new_expense.date == "2026-08-25"
    assert new_expense.description == "Bus"


def test_add_expense_defaults_date_to_today(sample_expenses):
    from datetime import date
    new_expense = operations.add_expense(sample_expenses, 10.0, "misc")

    assert new_expense.date == date.today().isoformat()


def test_add_expense_rejects_invalid_amount(sample_expenses):
    from cli_expense_tracker.exceptions import InvalidExpenseDataError
    with pytest.raises(InvalidExpenseDataError):
        operations.add_expense(sample_expenses, -5, "food","2026-01-01")


def test_delete_expense_removes_and_returns_it(sample_expenses):
    deleted = operations.delete_expense(sample_expenses, 3)
 
    assert deleted.id == 3
    assert deleted.category == "rent"
    assert len(sample_expenses) == 2
    assert all(e.id != 3 for e in sample_expenses)
 
 
def test_delete_expense_raises_for_missing_id(sample_expenses):
    with pytest.raises(ExpenseNotFoundError):
        operations.delete_expense(sample_expenses, 999)
 
 
def test_delete_expense_does_not_mutate_list_when_not_found(sample_expenses):
    original_length = len(sample_expenses)
    with pytest.raises(ExpenseNotFoundError):
        operations.delete_expense(sample_expenses, 999)
    assert len(sample_expenses) == original_length
 
 
def test_edit_expense_updates_only_amount(sample_expenses):
    updated = operations.edit_expense(sample_expenses, 1, amount=25.0)
 
    assert updated.amount == 25.0
    assert updated.category == "food"          
    assert updated.date == "2026-08-01"
    assert updated.description == "Lunch"
 
 
def test_edit_expense_updates_multiple_fields(sample_expenses):
    updated = operations.edit_expense(sample_expenses, 1, amount=30.0, category="groceries")
 
    assert updated.amount == 30.0
    assert updated.category == "groceries"
    assert updated.date == "2026-08-01"
 
 
def test_edit_expense_can_clear_description_with_empty_string(sample_expenses):
    updated = operations.edit_expense(sample_expenses, 1, description="")
    assert updated.description == ""
 
 
def test_edit_expense_raises_for_missing_id(sample_expenses):
    with pytest.raises(ExpenseNotFoundError):
        operations.edit_expense(sample_expenses, 999, amount=10.0)
 
 
def test_edit_expense_rejects_invalid_new_amount(sample_expenses):
    with pytest.raises(InvalidExpenseDataError):
        operations.edit_expense(sample_expenses, 1, amount=-10.0)
 
 
def test_edit_expense_with_no_fields_changes_nothing(sample_expenses):
    updated = operations.edit_expense(sample_expenses, 1)
 
    assert updated.amount == 20.0
    assert updated.category == "food"
    assert updated.date == "2026-08-01"
    assert updated.description == "Lunch"
 
 
def test_list_expenses_no_filters_returns_all(sample_expenses):
    result = operations.list_expenses(sample_expenses)
    assert len(result) == 3
 
 
def test_list_expenses_filters_by_category(sample_expenses):
    result = operations.list_expenses(sample_expenses, category="food")
    assert len(result) == 2
    assert all(e.category == "food" for e in result)
 
 
def test_list_expenses_filters_by_start_date(sample_expenses):
    result = operations.list_expenses(sample_expenses, start_date="2026-08-15")
    assert len(result) == 2
    assert all(e.date >= "2026-08-15" for e in result)
 
 
def test_list_expenses_filters_by_end_date(sample_expenses):
    result = operations.list_expenses(sample_expenses, end_date="2026-08-15")
    assert len(result) == 2
    assert all(e.date <= "2026-08-15" for e in result)
 
 
def test_list_expenses_filters_by_date_range(sample_expenses):
    result = operations.list_expenses(sample_expenses, start_date="2026-08-10", end_date="2026-08-20")
    assert len(result) == 2
 
 
def test_list_expenses_combines_category_and_date_filters(sample_expenses):
    result = operations.list_expenses(sample_expenses, category="food", start_date="2026-08-10")
    assert len(result) == 1
    assert result[0].id == 4
 
 
def test_list_expenses_empty_list_returns_empty():
    assert operations.list_expenses([]) == []
 
 
def test_list_expenses_does_not_mutate_original(sample_expenses):
    original_length = len(sample_expenses)
    operations.list_expenses(sample_expenses, category="food")
    assert len(sample_expenses) == original_length
 
 
def test_summarize_total(sample_expenses):
    result = operations.summarize(sample_expenses)
    assert result["total"] == 835.0
 
 
def test_summarize_by_category(sample_expenses):
    result = operations.summarize(sample_expenses)
    assert result["by_category"]["food"] == 35.0
    assert result["by_category"]["rent"] == 800.0
 
 
def test_summarize_empty_list():
    result = operations.summarize([])
    assert result["total"] == 0
    assert result["by_category"] == {}
 
