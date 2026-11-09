contacts = []
phones = set()


def add_contact(name, number):
    if number == "":
        print("enter a phone number")
        return
    elif name == "":
        print("enter a name")
        return
    elif number in phones:
        print("number already exist")
        return
    phones.add(number)

    contacts.append({"name": name, "number": number})
    print("contact save successfully")
    save_contacts()


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
            save_contacts()
            return
    print("contact does not exist")


def edit_contact(number):
    if number == "":
        print("input a phone number")
        return
    for contact in contacts:
        if contact["number"] == number:
            print(contact["name"])

            print("\n\nenter 1 to edit name")
            print("enter 2 to edit phone number")
            print("enter 3 to edit both name and phone number")

            user_choice = input("Please enter option 1-3: ")

            if user_choice == "1":
                new_name = input("please enter the new name: ")
                if new_name == "":
                    print("enter a name")
                    return
                contact["name"] = new_name

            elif user_choice == "2":
                new_phone = input("please enter the new phone number: ")
                if new_phone == "":
                    print("please enter a phone number")
                    return
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

                if new_name == "" or new_phone == "":
                    print("name and phone cannot be empty")
                    return
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
            save_contacts()
            return

    print("contact with that phone number does not exist")


def search_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            print(f"{contact['name']}, {contact['number']}")
            return

    print("\ncontact not found")


import json


def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)


def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            reload_contacts = json.load(file)
            for contact in reload_contacts:
                contacts.append(contact)
                phones.add(contact["number"])
    except FileNotFoundError:
        print("no saved contacts found")
