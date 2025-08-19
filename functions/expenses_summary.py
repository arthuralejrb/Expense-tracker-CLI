from functions.utils import read_expenses
from rich import print


def show_summary(args):
    """"""
    expenses = read_expenses()
    sum = 0

    if args.month:
        for expense in expenses:
            if (expense['date'][1] == args.month):
                sum += expense['amount']

        print(
            f'Total expenses in month {args.month}:[bold green]${sum}[/bold green]')
    else:
        for expense in expenses:
            sum += expense['amount']

        print(f'Total expenses:[bold green]${sum}[/bold green]')
