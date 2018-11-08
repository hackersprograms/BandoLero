from scapy.all import *
gonder = (IP(dst="192.168.1.1")/TCP(dport=80, flags="FS"))
send(gonder)
yakala = sniff(iface='wlan1', count=5)
yakala.nsummary()
ptk0=yakala[0]
pkt0.show()
