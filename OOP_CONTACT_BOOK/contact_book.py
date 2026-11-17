class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_all_contacts(self):
        for contact in self.contacts:
            contact.display_contact()

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                contact.display_contact()
                return
        print("Contact not found")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"{contact.name} deleted sucessfully")
                return
        print("contact not found")

    def edit_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print("Contact found\n")

                print("1. Change name")
                print("2. Change phone number")
                print("3. change email")

                user_selection = input("please choose from 1-3")
                if user_selection == "1":
                    new_name = input("enter new name")
                    if new_name != contact.name:
                        contact.name = new_name
                        print("name changed successfully")
                elif user_selection == "2":
                    new_number = input
                elif user_selection == "3":
                    print("changing email")
                else:
                    print("invalid selection")

                return
        print("Contact not found")
