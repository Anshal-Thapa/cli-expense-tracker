import json
from cli_expense_tracker.models import Expense

def save_expenses(expenses):
    json_data = []
    for each_expense in expenses:
        json_data.append(each_expense.to_dict())
    with open("./expenses.json","w",encoding="UTF-8") as f:
        json.dump(json_data,f)

def load_expenses():
    try:
        with open("./expenses.json","r",encoding="UTF-8") as f:
            json_data = json.load(f)
    except FileNotFoundError:
        return []
    data = []
    for each_json_data in json_data:
        data.append(Expense.from_dict(each_json_data))
    return data
