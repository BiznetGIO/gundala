from gundala import EPP, Contact
from config import contacts, config

epp = EPP(**config)
""" Get contact info. """
contact = Contact(epp, 7654322)
print(contact.info())
