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


menu_options = ("Add contact", "Display contacts", "Exit")

for item in menu_options:
    print(item)

for number in range(1, 6):
    print(number)
