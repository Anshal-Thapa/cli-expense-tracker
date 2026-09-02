from cli_expense_tracker.storage import save_expenses, load_expenses
from cli_expense_tracker.models import Expense


def test_save_and_load_round_trip(tmp_path):
    filepath = tmp_path / "expenses.json"
    expenses = [
        Expense(id=1, amount=20.0, category="food", date="2026-09-01", description="Lunch"),
        Expense(id=2, amount=800.0, category="rent", date="2026-09-01"),
    ]

    save_expenses(expenses, filepath)
    loaded = load_expenses(filepath)

    assert loaded == expenses

def test_load_expenses_missing_file_returns_empty_list(tmp_path):
    filepath = tmp_path / "does_not_exist.json"

    result = load_expenses(filepath)

    assert result == []


def test_save_expenses_overwrites_existing_file(tmp_path):
    filepath = tmp_path / "expenses.json"

    first_batch = [Expense(id=1, amount=20.0, category="food", date="2026-09-01")]
    save_expenses(first_batch, filepath)

    second_batch = [Expense(id=1, amount=50.0, category="rent", date="2026-09-01")]
    save_expenses(second_batch, filepath)

    loaded = load_expenses(filepath)

    assert loaded == second_batch


def test_save_empty_list(tmp_path):
    filepath = tmp_path / "expenses.json"

    save_expenses([], filepath)
    loaded = load_expenses(filepath)

    assert loaded == []
