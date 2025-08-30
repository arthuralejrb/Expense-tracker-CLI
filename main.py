import argparse
from functions.add_expense import add_expense
from functions.update_expense import update_expense
from functions.delete_expense import delete_expense
from functions.list_expenses import list_expenses
from functions.expenses_summary import show_summary
from functions.set_budget import set_budget
from functions.utils import convert_csv


parser = argparse.ArgumentParser(prog='Expense tracker')
subparsers = parser.add_subparsers(dest='commands', help="commands")


# parser arguments for add function
parser_add = subparsers.add_parser('add', help="Add an expense")

parser_add.add_argument('--amount', '--a',
                        help="Add expense value", type=float, required=True)

parser_add.add_argument('--description', '--d',
                        help="Describe the expense", type=str, required=True)

parser_add.add_argument('--category', '--c',
                        help="Add a category", type=str, required=False)


# parser arguments for updating a expense
parser_update = subparsers.add_parser('update', help="Update an expense")

parser_update.add_argument('--id',
                           help="Expense id to update", type=int,
                           required=True)

parser_update.add_argument('--amount', '--a',
                           help="Add expense value", type=float,
                           required=False)

parser_update.add_argument('--description', '--d',
                           help="Describe the expense", type=str,
                           required=False)

parser_update.add_argument('--category', '--c',
                           help="Add a category", type=str,
                           required=False)


# parser arguments for deleting a expense
parser_delete = subparsers.add_parser('delete', help="Delete an expense")

parser_delete.add_argument('--all',
                           help="Delete all expenses", required=False,
                           dest='all', action='store_true')

parser_delete.add_argument('--id',
                           help="Expense id to delete", type=int,
                           required=False)


# parser arguments for listing expenses
parser_list = subparsers.add_parser('list',
                                    help="List all expenses")

parser_list.add_argument('--category', '--c',
                         help="List all expenses by category", required=False,)

# parser arguments for showing a summary of all expenses
parser_summary = subparsers.add_parser('summary',
                                       help="Show a summary of all expenses")

parser_summary.add_argument('--month', '--m',
                            help="Show a summary of all expenses from a given month",
                            required=False)


parser_budget = subparsers.add_parser('budget',
                                      help="Set a budget for a given month")
parser_budget.add_argument('--month', '--m',
                           help="Specify the month",
                           required=True)

parser_budget.add_argument('--amount', '--a',
                           help="Set the budget amount",
                           required=True)


parser_csv = subparsers.add_parser('csv',
                                   help="Exports data to a .CSV file")


args = parser.parse_args()
command = args.commands

match (command):
    case 'add':
        add_expense(args)
    case 'update':
        update_expense(args)
    case 'delete':
        delete_expense(args)
    case 'list':
        list_expenses(args)
    case 'summary':
        show_summary(args)
    case 'budget':
        set_budget(args)
    case 'csv':
        convert_csv()
