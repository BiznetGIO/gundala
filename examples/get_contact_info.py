from gundala import EPP, Contact
from config import contacts, config

epp = EPP(**config)

contact = Contact(epp, 7654322)
print(contact.info())
