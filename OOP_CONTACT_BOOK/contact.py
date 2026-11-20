class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def display_contact(self):
        print(self.name, self.phone_number, self.email)

    def to_dict(self):
        return {
            "name": self.name,
            "phone_number": self.phone_number,
            "email": self.email,
        }
