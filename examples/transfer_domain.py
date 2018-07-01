from gundala import EPP, Domain
from config import config, contacts, namespaces

epp = EPP(**config)
domain = Domain(epp, 'hatiku.id')
domain.transfer(domain.token())
