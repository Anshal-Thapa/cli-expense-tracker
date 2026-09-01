import json
import Exception
from cli_expense_tracker.models import Expense

def save_expenses(expenses,filepath):
    json_data = []
    for each_expense in expenses:
        json_data.append(each_expense.to_dict())
    with open(filepath,"w",encoding="UTF-8") as f:
        json.dump(json_data,f,indent)

def load_expenses(filepath):
    try:
        with open(filepath,"r",encoding="UTF-8") as f:
            json_data = json.load(f)
    expect FileNotFoundError:
        return []
    data = []
    for each_json_data in json_data:
        data.append(Expense.from_dict(each_json_data))
    return data
