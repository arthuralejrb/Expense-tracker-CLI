from functions.utils import write_expense, read_expenses
from rich import print


def add_expense(args):
    """Adds expense to .json file"""

    expenses = read_expenses()

    if len(expenses) > 0:
        expense_id = expenses[-1]["id"] + 1
    else:
        expense_id = 1

    expenses.append({
        "id": expense_id,
        "amount": args.amount,
        "category": args.category,
        "description": args.description,
    })

    write_expense(expenses)

    print("[bold green]Expense added successfully![/bold green]")
    print(f"[bold blue]ID:{expense_id}[/bold blue]")
