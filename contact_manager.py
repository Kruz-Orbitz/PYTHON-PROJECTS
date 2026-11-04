contacts = []
phones = set()


def add_contact(name, number):
    if number in phones:
        print("number already exist")
        return
    phones.add(number)

    contacts.append({"name": name, "number": number})


def display_contacts():
    if contacts == []:
        print("there is no contact")
    else:
        for contact in contacts:
            print(f"{contact['name']}, {contact['number']}")


def delete_contact(number):
    for contact in contacts:
        if number == contact["number"]:
            contacts.remove(contact)
            phones.remove(number)
            print("details removed successfully")
            return
    print("contact does not exist")


def edit_contact(number):
    for contact in contacts:
        if contact["number"] == number:
            print(contact["name"])

            print("\n\nenter 1 to edit name")
            print("enter 2 to edit phone number")
            print("enter 3 to edit both name and phone number")

            user_choice = input("Please enter option 1-3: ")

            if user_choice == "1":
                new_name = input("please enter the new name: ")
                contact["name"] = new_name

            elif user_choice == "2":
                new_phone = input("please enter the new phone number: ")
                if new_phone in phones and new_phone != number:
                    print("phone number already exist")
                    return
                if new_phone != number:
                    phones.remove(number)
                    phones.add(new_phone)
                    contact["number"] = new_phone

            elif user_choice == "3":
                new_name = input("please enter new name: ")
                new_phone = input("please enter new phone: ")
                if new_phone in phones and new_phone != number:
                    print("phone number already exist")
                    return
                contact["name"] = new_name
                if new_phone != number:
                    phones.remove(number)
                    phones.add(new_phone)
                    contact["number"] = new_phone

            else:
                print("enter a valid number")
                return

            print("contact saved successfully")
            return

    print("contact with that phone number does not exist")
