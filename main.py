from network_scanner import NetworkScanner
from mac_finder import MacFinder
from datetime import date
from device import Device
import argparse

"""
Network Scanner
    José Victor Viriato 
    Lana Rossato
Instalação:
    pip install -r requirements.txt
Exemplo de uso:
    (necessário permissão root)
    sudo python3 main.py --ip '192.168.1.103/24'
"""

def parseArguments():
    parser = argparse.ArgumentParser(description='Recebe o IP do usuário (c/ subnet mask).')    
    parser.add_argument('--ip', metavar='i', type=str,
                    help='Recebe o IP do usuário (c/ subnet mask).', required=True)
    return parser.parse_args()

def parseDevices(clients):
    devices = []
    mac_finder = MacFinder()
    for client in clients:
        devices.append(Device(ip = client['ip'],
                              mac = client['mac'], 
                              manufacturer = mac_finder.getManufacturer(client['mac']),
                              isHost = False))
    return devices

def printDevices(devices):
    for device in devices:
        print(device)

def main():
    args = parseArguments()
    net = NetworkScanner(args.ip)
    clients = net.scan()
    devices = parseDevices(clients)
    printDevices(devices)


if __name__ == "__main__":
    main()