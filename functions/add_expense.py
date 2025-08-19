from functions.utils import write_expense, read_expenses
from rich import print
from datetime import datetime


def add_expense(args):
    """Adds expense to .json file"""

    expenses = read_expenses()

    if len(expenses) > 0:
        expense_id = expenses[-1]["id"] + 1
    else:
        expense_id = 1

    date = datetime.now()

    expenses.append({
        "id": expense_id,
        "amount": args.amount,
        "category": args.category,
        "description": args.description,
        "date": date.strftime("%mm/%dd/%yy")
    })

    write_expense(expenses)

    print(
        f"[bold green]Expense added successfully![/bold green] [bold blue]ID:{expense_id}[/bold blue]")
