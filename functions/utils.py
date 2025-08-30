import json
import csv
import os

json_filename = ['expenses.json', 'budgets.json']
csv_filename = 'expenses.csv'


def read_expenses():
    """open and reads a expenses json file or creates one if neccessary"""

    try:
        if os.path.exists(json_filename[0]):
            with open(json_filename[0], 'r') as f:
                return json.load(f)
        return []
    except json.JSONDecodeError:
        return []


def write_expense(expense):
    """Writes changes in expenses json file"""

    with open(json_filename[0], 'w') as json_file:
        json.dump(expense, json_file, indent=3)


def read_budget():
    """open and reads a budgets json file or creates one if neccessary"""

    try:
        if os.path.exists(json_filename[1]):
            with open(json_filename[1], 'r') as f:
                return json.load(f)
        return []
    except json.JSONDecodeError:
        return []


def write_budget(budget):
    """Writes changes in budgets json file"""

    with open(json_filename[1], 'w') as json_file:
        json.dump(budget, json_file, indent=3)


def convert_csv():
    """exports all data in json file to csv file"""

    with open(csv_filename, 'w') as f:
        writer = csv.writer(f)
        expenses = read_expenses()
        c = 0

        for expense in expenses:

            if c == 0:
                keys = expense.keys()
                writer.writerow(keys)
                c += 1

            writer.writerow(expense.values())
