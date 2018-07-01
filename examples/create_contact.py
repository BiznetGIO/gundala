from gundala import EPP
from config import config, contacts, namespaces

epp = EPP.EPP(**config)

data = {
    'id': '7654322',
    'name': 'Admin 2',
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

contact = EPP.Contact(epp, False, **data)
print(contact.create())