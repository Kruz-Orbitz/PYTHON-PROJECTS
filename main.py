from contact_manager import add_contact, display_contacts, delete_contact, edit_contact

while True:
    print("\n=== MAIN MENU===")

    main_options = (
        "Add contact",
        "Display contacts",
        "Delete contact",
        "Edit contact" "Exit",
    )
    for option in range(len(main_options)):
        print(option + 1, main_options[option])

    user_choice = input("Please enter your prefered choice 1-4: ")
    if user_choice == "1":
        name = input("please enter a name: ")
        number = input("please enter the phone number: ")
        add_contact(name, number)

    elif user_choice == "2":
        display_contacts()
    elif user_choice == "3":
        number = input("Please enter the number to be deleted: ")
        delete_contact(number)

    elif user_choice == "4":
        print("alright this is the end")
        break
    else:
        print("input a valid option")
