from functions.utils import read_expenses
from rich import print
from rich.table import Table
from rich.console import Console


def list_expenses(args):
    """Show all expenses in json file"""

    expenses = read_expenses()

    table = Table(title="Expense List")
    table.add_column("ID", justify='right', style='cyan', no_wrap=True)
    table.add_column("Description", style='red')
    table.add_column("Amount", style='green')
    table.add_column("Category", style='cyan')
    table.add_column("Date", justify='right', style='cyan')

    if (args.category):
        for expense in expenses:
            if expense['category'] == args.category:
                table.add_row(
                    str(expense['id']),
                    expense['description'],
                    str(expense['amount']),
                    expense['category'],
                    expense['date'],
                )
    else:
        for expense in expenses:
            table.add_row(
                str(expense['id']),
                expense['description'],
                str(expense['amount']),
                expense['category'],
                expense['date'],
            )
    console = Console()
    console.print(table)
