from gundala import EPP
from config import config

epp = EPP.EPP(**config)

domain = EPP.Domain(epp, 'hatiku.id')
domain.info()
print(domain.roid)
print(domain.status)