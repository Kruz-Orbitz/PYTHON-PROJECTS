import json
from contact import Contact


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()

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
                self.save_contacts()
                return
        print("contact not found")

    def edit_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print("Contact found\n")

                print("1. Change name")
                print("2. Change phone number")
                print("3. change email")

                user_selection = input("please choose from 1-3: ")
                if user_selection == "1":
                    new_name = input("enter new name: ").strip()
                    if new_name == "":
                        print("please enter a valid name")
                        return
                    elif new_name != contact.name:
                        contact.name = new_name
                        self.save_contacts()
                        print("name changed successfully")
                    else:
                        print("name already the current name")
                elif user_selection == "2":
                    new_number = input("please enter a new phone number: ").strip()
                    if new_number == "":
                        print("please enter a valid phone number")
                        return
                    elif new_number == contact.phone_number:
                        print("phone  number already the current number")
                        return
                    for duplicate in self.contacts:
                        if (
                            duplicate.phone_number == new_number
                            and duplicate is not contact
                        ):
                            print("number already exist")
                            return
                    contact.phone_number = new_number
                    self.save_contacts()
                    print("number updated successfully")
                elif user_selection == "3":
                    new_email = input("enter a new email address: ").strip()
                    if new_email == "":
                        print("please enter a valid email address")
                        return
                    elif new_email == contact.email:
                        print("email already the current email")
                        return
                    for duplicate in self.contacts:
                        if duplicate.email == new_email and duplicate is not contact:
                            print("email already exist")
                            return
                    contact.email = new_email
                    self.save_contacts()
                    print("email address successfully changed")
                    

                else:
                    print("invalid selection")
                    

                return
                
        print("Contact not found")

    def save_contacts(self):
        dict_data = []
        for contact in self.contacts:
            dict_data.append(contact.to_dict())

        with open("contacts.json", "w") as file:
            json.dump(dict_data, file, indent=4)

    def load_contacts(self):
        try:
            with open("contacts.json", "r") as file:
                dict_files = json.load(file)
        except FileNotFoundError:
            print('no saved contacts yet')
            self.contacts = []
            return

        for contact in dict_files:
            contact_data = Contact(contact["name"], contact["phone_number"], contact["email"])
            self.contacts.append(contact_data)
