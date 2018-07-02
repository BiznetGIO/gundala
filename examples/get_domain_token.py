from gundala import EPP, Domain
from config import config

epp = EPP(**config)
""" Get token for a given domain """
domain = Domain(epp, 'gundala.id')
print(domain.token())
