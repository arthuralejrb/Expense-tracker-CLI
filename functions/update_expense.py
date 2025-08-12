from functions.utils import write_expense, read_expenses
from rich import print


def update_expense(args):
    """"""

    expenses = read_expenses()

    if args.amount:
        expenses[args.id - 1]["amount"] = args.amount
    if args.description:
        expenses[args.id - 1]["description"] = args.description
    if args.category:
        expenses[args.id - 1]["category"] = args.category

    write_expense(expenses)
    print(
        f"[bold green]Expense ID:[bold blue]{args.id}[/bold blue] was successfully updated![/bold green]")
