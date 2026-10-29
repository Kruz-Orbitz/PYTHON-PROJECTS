
def display_expenses(expenses):
    for item in expenses:
        print(f"{item['description']} {item['amount']}")


def calculate_total(expenses):

    total = 0

    for item in expenses:
        total += item["amount"]
    return total

import json

expenses = [
    {"description": "television", "amount": 200},
    {"description": "phone", "amount": 500},
    {"description": "laptop", "amount": 300},
    {"description": "data", "amount": 1500},
]

with open('expenses.json', 'w') as file:
    json.dump(expenses, file, indent=4)


with open('expenses.json', 'r') as file:
    loaded_expenses = json.load(file)

add_expense = {'description': 'mouse', 'amount': 250}

loaded_expenses.append(add_expense)

with open('expenses.json', 'w')as file:
    json.dump(loaded_expenses, file, indent=4)

with open('expenses.json', 'r')as file:
    updated_expenses = json.load(file)
print(updated_expenses)
    


import json

try:
    with open('expenses.json', 'r')as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = []
except ValueError:
    print('invalid json file')
    expenses = []
print(expenses)

added_expenses = {'description': 'keyboard', 'amount': 750}

expenses.append(added_expenses)

with open('expenses.json', 'w') as file:
    json.dump(expenses, file, indent=4)