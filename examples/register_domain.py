from gundala import EPP
from config import config, contacts, namespaces

epp = EPP.EPP(**config)
domain = EPP.Domain(epp, 'hatiku.id')
domain.create(contacts, namespaces[0])