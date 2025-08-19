from functions.utils import read_expenses
from rich import print


def list_expenses():
    """"""

    expenses = read_expenses()
    print("[bold blue]ID[/bold blue]\t\t[bold red]Description[/bold red]\t\t[bold green]Amount[/bold green]\n")

    for expense in expenses:
        print(f'[bold blue]{expense['id']}[/bold blue]\t\t[bold red]{expense['description']}[/bold red]\t\t\t[bold green]${expense['amount']}[/bold green]')
