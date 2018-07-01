from gundala import EPP, Domain
from config import config

epp = EPP(**config)
""" Get the token for a given domain """
domain = Domain(epp, 'segokucing.id')
print(domain.token())
