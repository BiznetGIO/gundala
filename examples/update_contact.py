from gundala import EPP, Contact
from config import config, contacts, nameserver

data = {
    'name': 'Admin 2 updated',
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
""" Update contact. """
contact = Contact(epp, 7654322, **data)
print(contact.update())