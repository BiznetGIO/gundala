from gundala import EPP
from config import config, contacts, namespaces

epp = EPP.EPP(**config)

contact = EPP.Contact(epp, 7654322)
print(contact.info())
