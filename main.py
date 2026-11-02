main_options = ("Add contact", "Display contacts", "Exit")

for option in range(len(main_options)):
    print(option + 1, main_options[option])

user_choice = int((input("Please enter your prefered choice 1-3: ")))

if user_choice == 1:
    print("Add contact")
elif user_choice == 2:
    print("Display contacts")
elif user_choice == 3:
    print("Exit")
else:
    print("invalid number option")
