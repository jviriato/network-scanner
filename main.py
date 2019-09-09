import argparse
from network_scanner import NetworkScanner
from mac_finder import MacFinder
from device import Device
from writer import Writer
import time
"""
Network Scanner
    José Victor Viriato 
    Lana Rossato
Instalação:
    pip install -r requirements.txt
Exemplo de uso:
    (necessário permissão root)
    sudo python3 main.py --ip '192.168.1.1/24' --time 1
"""

def parseArguments():
    parser = argparse.ArgumentParser(description='--help para mais infos.')    
    parser.add_argument('--ip', 
                        metavar='i', 
                        type=str,
                        help='Recebe o IP (c/ subnet mask).', 
                        required=True)
    parser.add_argument('--time', 
                        metavar='t', 
                        type=float,
                        help='O intervalo de tempo (em minutos) que será realizado o scan.', 
                        required=True)
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
    w = Writer()
    while(True):
        clients = net.scan()
        devices = parseDevices(clients)
        printDevices(devices)
        w.writeToCSV(devices)
        time.sleep(60 * args.time)

if __name__ == "__main__":
    main()