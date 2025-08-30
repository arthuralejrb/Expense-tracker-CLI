from functions.utils import read_expenses
from rich import print


def show_summary(args):
    """Show a summary of all the expenses"""

    expenses = read_expenses()
    sum = 0

    if args.month:
        month_summary(args.month, expenses)
    else:
        for expense in expenses:
            sum += expense['amount']

    print(f'Total expenses:[bold green]${sum}[/bold green]')


def month_summary(month, expenses):
    """"""

    sum = 0

    for expense in expenses:
        if (expense['date'][1] == month):
            sum += expense['amount']

        return sum
