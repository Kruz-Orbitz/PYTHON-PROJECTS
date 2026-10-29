from expenses_function import expenses, display_expenses, calculate_total


while True:
    print("1. view expenses")
    print("2. view total")
    print("3.exit")

    make_your_choice = input("choose an option 1-3: ").strip()

    if make_your_choice == "1":
        display_expenses(expenses)

    elif make_your_choice == "2":
        total = calculate_total(expenses)
        print(f'total expenses: {total}')

    elif make_your_choice == "3":
        break
    else:
        print("input a valid number 1-3")
