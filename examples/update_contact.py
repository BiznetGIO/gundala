from gundala import EPP
from config import config, contacts, namespaces

epp = EPP.EPP(**config)

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

contact = EPP.Contact(epp, 7654322, **data)
print(contact.update())
