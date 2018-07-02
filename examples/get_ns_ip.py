from gundala import EPP, Nameserver
from config import config, nameserver

epp = EPP(**config)
""" Get the ip address for a given nameserver """
ns = Nameserver(epp, nameserver[0])
print(ns.get_ip())
