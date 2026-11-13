class Contact:
    def __init__(self, name, number):
        self.name = name
        self.__number = number

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, new_number):
        if new_number == "":
            print("enter a phone number")
        else:
            self.__number = new_number

    def display_contact(self):
        print(f"{self.name} {self.__number}")


kingsley = Contact("kingsley", "08033443344")
amara = Contact("amara", "08334433444")

kingsley.display_contact()
amara.display_contact()
kingsley.number = ""
kingsley.number = "08034699420"
kingsley.display_contact()

# INHERITANCE


class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def display_contact(self):
        print(self.name, self.number)


class BusinessContact(Contact):
    def __init__(self, name, number, company):
        super().__init__(name, number)
        self.company = company

    def display_company(self):
        print(self.company)


kingsley = BusinessContact("kingsley", "08034699420", "Talent Naton")
kingsley.display_contact()
kingsley.display_company()


class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def display_contact(self):
        print(self.name, self.number)


class BusinessContact(Contact):
    def __init__(self, name, number, company):
        super().__init__(name, number)
        self.company = company

    def display_contact(self):
        print("Business Contact:", self.name, self.number)


person = Contact("kingsley", "99444333")

business = BusinessContact("kingsley", "08034699420", "Talent Naton")

person.display_contact()
business.display_contact()


# POLYMORPHISM
class Contact:
    def display_type(self):
        print("Normal Contact")


class BusinessContact:
    def display_type(self):
        print("Business Contact")


personal = Contact()
business = BusinessContact()

personal.display_type()
business.display_type()


# POLYMORPHISM AND INHERITANCE
class Contact:
    def display_type(self):
        print("Normal Contact")


class BusinessContact(Contact):
    def display_type(self):
        print("Business Contact")


personal = Contact()
business = BusinessContact()

personal.display_type()
business.display_type()


# POLYMORPHISM: DOCK TYPING
# python can display objects independ information
# even though they share the same method
class Contact:
    def display(self):
        print("Displaying personal contact")


class BusinessContact:
    def display(self):
        print("Displaying business Contact")


class EmergencyContact:
    def display(self):
        print("Displaying emergency contact")


contact = Contact()
business = BusinessContact()
emergency = EmergencyContact()

contact.display()
business.display()
emergency.display()


# coding exercise in dock typing
class Contact:
    def display_contact(self):
        print("normal contact")


class BusinessContact:
    def display_contact(self):
        print("Business contact")


class EmergencyContact:
    def display_contact(self):
        print("Emergency contact")


contact = Contact()
business = BusinessContact()
emergency = EmergencyContact()

contacts = [contact, business, emergency]

for contact in contacts:
    contact.display_contact()

# Composition


class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


phone = Phone("Samsung", "S24")
person = Person("Kingsley", phone)

print(person.name)
print(person.phone.brand)
print(person.phone.model)


# composition codding exercise
class Battery:
    def __init__(self, capacity, battery_type):
        self.capacity = capacity
        self.battery_type = battery_type


class Laptop:
    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery


battery = Battery("4000mah", "Toshiba")
laptop = Laptop("Dell", battery)

print(laptop.brand)
print(laptop.battery.capacity)
print(laptop.battery.battery_type)

"""
Understanding Dunder Method
understanding __str__(), __repr__()  and __len__()
"""


class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def __str__(self):
        return f"name: {self.name}, course: {self.course}"


student1 = Student("ngozi", "hamatology")
student2 = Student("uchechi", "histology")

print(student1)
print(student2)


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"the book title is: {self.title} by: {self.author})"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"


book = Book("the gods are wise", "Chinua Achebe")

print(book)
print(repr(book))


class ShoppingCart:
    def __init__(self, goods):
        self.goods = goods

    def __len__(self):
        return len(self.goods)


cat_items = ShoppingCart(["milk", "millo", "bread", "wine", "bag"])

print(len(cat_items))

cat_items.goods.append("cup")

print(len(cat_items))
