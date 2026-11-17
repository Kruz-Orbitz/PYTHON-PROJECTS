from contact import Contact
from contact_book import ContactBook


kingsley = Contact("kingsley", "080334433223", "kingsley234@gmail.com")
mary = Contact("mary", "090332233443", "mary222@gmail.com")
tega = Contact("tega", "9933443233", "tega332@gmail.com")

my_book = ContactBook()
my_book.add_contact(kingsley)
my_book.add_contact(mary)
my_book.add_contact(tega)

my_book.search_contact('mary')
my_book.search_contact('david')

my_book.delete_contact('mary')
my_book.display_all_contacts()
my_book.delete_contact('david')

my_book.edit_contact('kingsley')