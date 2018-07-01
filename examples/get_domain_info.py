from gundala import EPP, Domain
from config import config

epp = EPP.EPP(**config)

domain = Domain(epp, 'hatiku.id')
domain.info()
print(domain.roid)
print(domain.status)
