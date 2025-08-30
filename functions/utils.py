import json
import os

filename = ['expenses.json', 'budgets.json']


def read_expenses():
    """open and reads a json file or creates one if neccessary"""
    try:
        if os.path.exists(filename[0]):
            with open(filename[0], 'r') as f:
                return json.load(f)
        return []
    except json.JSONDecodeError:
        return []


def write_expense(expense):
    """Writes changes in expenses json file"""

    with open(filename[0], 'w') as json_file:
        json.dump(expense, json_file, indent=3)


def read_budget():
    """"""
    try:
        if os.path.exists(filename[1]):
            with open(filename[1], 'r') as f:
                return json.load(f)
        return []
    except json.JSONDecodeError:
        return []


def write_budget(budget):
    """"""

    with open(filename[1], 'w') as json_file:
        json.dump(budget, json_file, indent=3)
