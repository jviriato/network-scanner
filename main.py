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
Argumentos:
    --time: De quanto em quanto tempo (em minutos) é realizado o scan. Ex: --time 15
    --ip: Passar o ip e máscara como argumento. Ex: --ip '192.168.1.1/24'
    --interface: Passar interface (para descobrir o IP, máscara e end. do router) Ex: --interface wlp6s0
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

def compareDevices(devices, csv_devices):
    for device in devices:
        if (any(d.mac == device.mac for d in csv_devices)):
            device.status = "Online"
        else:
            device.status = "Novo"
    return list(set(devices + csv_devices))
        

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
        csv_devices = w.getDevicesFromCSV()
        list_to_print = compareDevices(devices, csv_devices)
        printDevices(list_to_print)
        w.writeToCSV(devices)
        time.sleep(60 * args.time)

if __name__ == "__main__":
    main()