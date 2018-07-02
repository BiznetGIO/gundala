from gundala import EPP, Domain
from config import config

epp = EPP(**config)
""" Get the availability for a given domain. """
domain = Domain(epp, 'gundala.id')
print('Domain is available' if domain.available() else 'Domain is not available')
