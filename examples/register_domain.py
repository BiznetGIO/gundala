from gundala import EPP, Domain
from config import config, contacts, nameserver

epp = EPP(**config)
""" Register domain """
domain = Domain(epp, 'gundala.id')
domain.create(contacts, nameserver[0])
