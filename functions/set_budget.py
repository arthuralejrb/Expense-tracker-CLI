from functions.utils import read_budget, write_budget, read_expenses
from functions.expenses_summary import month_summary
from rich import print


def show_budget(args):
    """Show the budget situation"""

    expenses = read_expenses()

    sum = int(month_summary(args.month, expenses))

    if sum >= int(args.amount):
        print(
            f'[bold red]WARNING![/bold red]month budget exceeded: $${sum}/$${args.amount}')
    elif sum >= int(args.amount) * 0.8:
        print(
            f'[bold red]Warning![/bold red]month budget almost exceeded: $${sum}/$${args.amount}')
    else:
        print(f'Month budget: $${sum}/$${args.amount}')

    set_budget(args)


def set_budget(args):
    """Inserts a new budget in the budgets.json file"""
    budgets = read_budget()

    for i in range(0, len(budgets)):
        if budgets[i]["month"] == args.month:
            budgets.pop(i)

    budgets.append({
        'month': args.month,
        'amount': args.amount,
    })

    write_budget(budgets)
