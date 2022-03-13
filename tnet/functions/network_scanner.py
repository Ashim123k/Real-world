import scapy.all as scapy
def Scan(ip):
    arp_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast_packet = broadcast_packet/arp_packet
    answered_list = scapy.srp(arp_broadcast_packet, timeout=1, verbose=False)[0]
    client_list = []

    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)

    return client_list

def print_result(scan_list):
    print("IP\t\t\tMAC\n----------------------------------------")
    for client in scan_list:
        print(client["ip"] + "\t\t" + client["mac"])

#result_list=scan("11.0.0.1/24")
#print_result(result_list)
