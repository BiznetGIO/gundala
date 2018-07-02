from gundala import EPP, Domain
from config import config

epp = EPP(**config)
""" Get domain info. """
domain = Domain(epp, 'gundala.id')
domain.info()
print(domain.roid)
print(domain.status)
