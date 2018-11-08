from scapy.all import *

gonder = (IP(dst="192.168.1.1")/TCP(sport=4444, dport=80, flags="FS"))
send(gonder)
yakala = sniff(iface="wlan1", count=5)
yakala.nsummary()
ptk0=yakala[0]
ptk0.show()

srloop(IP(dst="192.168.1.1")/ICMP(), count=100)

yakala = sniff(filter="arp", count=100)
yakala.nsummary()
ptks0=yakala[0]
ptks0.show()


