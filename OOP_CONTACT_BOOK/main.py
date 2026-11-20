from contact import Contact
from contact_book import ContactBook


my_book = ContactBook()
my_book.load_contacts()

while True:
    print("\n=== MAIN MENU===")

    main_options = (
        "Add contact",
        "Display all contacts",
        "Search contact",
        "Edit contact",
        "Delete contact",
        "Exit",
    )
    for option in range(len(main_options)):
        print(option + 1, main_options[option])

    user_choice = input("Please enter your prefered choice 1-6: ")
    if user_choice == "1":
        name = input("please enter a name: ").strip()
        phone = input('please enter a phone number: ').strip()
        email = input('please enter an email address: ').strip()
        my_book.add_contact(Contact(name, phone, email))

    elif user_choice == "2":
        my_book.display_all_contacts()
    elif user_choice == "3":
        contact = input("Please enter the name to search: ")
        my_book.search_contact(contact)
    elif user_choice == "4":
        contact = input("please enter your existing contact to edit: ")
        my_book.edit_contact(contact)
    elif user_choice == "5":
        name = input("please enter the name: ")
        my_book.delete_contact(name)
    elif user_choice == "6":
        print("alright this is the end")
        break
    else:
        print("input a valid option")
