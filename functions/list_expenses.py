from functions.utils import read_expenses
from rich import print


def list_expenses():
    """"""

    expenses = read_expenses()

    for expense in expenses:
        print(expense)
