import json

try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = []
except ValueError:
    print("invalid file")
    expenses = []


def display_expenses(expenses):
    for item in expenses:
        print(f"{item['description']} {item['amount']}")


def calculate_total(expenses):
    total = 0

    for item in expenses:
        total += item["amount"]
    return total


while True:
    print('press "1" to view expenses')
    print('press "2" to view to view total')
    print('press "3" to add new expenses')
    print('press "4" to exit')

    choice = input("please enter number 1-4")

    if choice == "1":
        display_expenses(expenses)
    elif choice == "2":
        display_total = calculate_total(expenses)
        print(f"total expenses: {display_total}")
    elif choice == "3":
        description = input("input description").strip()
        try:
            amount = float(input("input amount"))
        except ValueError:
            print("input a valid number")
        new_expenses = {"description": description, "amount": amount}
        expenses.append(new_expenses)

        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)
    elif choice == "4":
        break
    else:
        print("input a valid number")
