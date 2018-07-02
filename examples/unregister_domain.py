from gundala import EPP, Domain
from config import config, contacts, nameserver

epp = EPP(**config)
""" Unregister domain. """
domain = Domain(epp, 'gundala.id')
domain.delete()
