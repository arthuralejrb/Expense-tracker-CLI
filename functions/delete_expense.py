from functions.utils import write_expense, read_expenses
from rich import print


def delete_expense(args):
    """Deletes specific expense from json file"""

    expenses = read_expenses()

    if args.all:
        expenses.clear()
        write_expense(expenses)

    else:
        expenses.pop(args.id - 1)

        update_ids(expenses, args)

        print(
            f"[bold green]The expense [bold blue]ID:{args.id}[/bold blue] was successfully deleted![/bold green]")


def update_ids(expenses, args):
    """update the ids of all expenses in json file"""

    for i in range(args.id - 1, len(expenses)):
        expenses[i]["id"] = i + 1

    write_expense(expenses)
