from gundala import EPP
from config import config

epp = EPP.EPP(**config)
""" Get the token for a given domain """
domain = EPP.Domain(epp, 'segokucing.id')
print(domain.available())