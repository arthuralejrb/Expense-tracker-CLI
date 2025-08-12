import json
import os

filename = 'expenses.json'


def read_expenses():
    """"""
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                return json.load(f)
        return []
    except json.JSONDecodeError:
        return []


def write_expense(expense):
    """"""

    with open(filename, 'w') as json_file:
        json.dump(expense, json_file, indent=3)
