
import socket
import scapy.all as scapy
class NetworkScanner:
    """ Classe para realizar o scan da rede.
    """
    def __init__(self, ip):
        self.ip = ip

    def scan(self):
        """ Realiza o scan da rede e retorna
                
        Returns:
            Array -- Uma array de clientes
        """
        arp_request = scapy.ARP(pdst=self.ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=12,
                              verbose=True)[0]
        clients_list = []
        for element in answered_list:
            client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
            clients_list.append(client_dict)
        return clients_list