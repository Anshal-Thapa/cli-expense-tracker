import argparse
from cli_expense_tracker import operations
from cli_expense_tracker import storage
from cli_expense_tracker.exceptions import AppError

EXPENSES = "./expenses.json"

def main():
    parser = argparse.ArgumentParser(description="CLI EXPENSE TRACKER")
    subparser = parser.add_subparsers(dest="command",required=True)

    parser_add = subparser.add_parser("add",help="Add Expenses")
    parser_add.add_argument("--amount",type=float,required=True)
    parser_add.add_argument("--category",required=True)
    parser_add.add_argument("--date",dest="expense_date")
    parser_add.add_argument("--desc",dest="description",default="")

    parser_list = subparser.add_parser("list",help="Views all/filtered expenses based on category and date range")
    parser_list.add_argument("--category")
    parser_list.add_argument("--from",dest="start_date")
    parser_list.add_argument("--to",dest="end_date")

    parser_delete = subparser.add_parser("del",help="Delete Expenses with id")
    parser_delete.add_argument("--id",type=int,required=True)

    parser_edit = subparser.add_parser("edit",help="Edit Expenses")
    parser_edit.add_argument("--id",type=int,required=True)
    parser_edit.add_argument("--amount",type=float)
    parser_edit.add_argument("--category")
    parser_edit.add_argument("--date",dest="expense_date")
    parser_edit.add_argument("--desc",dest="description")

    subparser.add_parser("summary",help="Provides summary of overall as well as category wise.")

    args = parser.parse_args()

    expenses = storage.load_expenses(EXPENSES)

    try:
        if args.command == "add":
            new_expense = operations.add_expense(expenses, args.amount, args.category,args.expense_date,args.description)
            storage.save_expenses(expenses,EXPENSES)
            print(f"Expence added #{new_expense.id}: Rs.{new_expense.amount:.2f} - {new_expense.category}")
        elif args.command == "list":
            result = operations.list_expenses(expenses,args.category,args.start_date,args.end_date)
            if not result:
                print("No expenses in record.")
            else:
                for expense in result:
                    print(f"{expense.id:>3}  Rs.{expense.amount:>8.2f}  {expense.category:<8} {expense.date}  {expense.description}")

        elif args.command == "del":
            new_expense = operations.delete_expense(expenses,args.id)
            storage.save_expenses(expenses,EXPENSES)
            print(f"Expence Deleted #{new_expense.id}: Rs.{new_expense.amount:.2f} - {new_expense.category}")


        elif args.command == "edit":
            new_expense = operations.edit_expense(expenses,args.id,args.amount,args.category,args.expense_date,args.description)
            storage.save_expenses(expenses,EXPENSES)
            print(f"Expence edited #{new_expense.id}: Rs.{new_expense.amount:.2f} - {new_expense.category}")


        elif args.command == "summary":
            result = operations.summarize(expenses)
            print(f"Total Expenses: {result["total"]}")
            for category, total in result["by_category"].items():
                print(f"Expense for {category}: {total}")

    except AppError as e:
        print(f"Error: {e}")
