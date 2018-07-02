from gundala import EPP, Contact
from config import config, contacts, nameserver

data = {
    'id': '7654323',
    'name': 'Admin 3',
    'org': 'Biznetgio',
    'street': 'Jl. Sudirman',
    'city': 'Jakarta Pusat',
    'sp': '',
    'pc': '',
    'cc': 'ID',
    'voice': '',
    'fax': '',
    'email': 'admin@biznetgio.com',
}
epp = EPP(**config)
""" Create new contact. """
contact = Contact(epp, False, **data)
print(contact.create())