from gundala import EPP, Domain
from config import config, contacts, nameserver

epp = EPP(**config)
""" Transfer domain """
domain = Domain(epp, 'gundala.id')
domain.transfer(domain.token())
