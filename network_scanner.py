
import subprocess
import socket
import csv
import os
from datetime import date
from mac_finder import MacFinder
from device import Device
class NetworkScanner:
    """ Classe para realizar o scan da rede.
    """
    def __init__(self):
        self.today = date.today()

    def getOwnIpAddress(self):
        """Retorna o IP do usuário
        Returns:
            str -- IP do usuário formatado
        """
        hostname = socket.gethostname()
        ipAddr = socket.gethostbyname(hostname)
        return ipAddr
    
    def createCSV(self):
        """ Cria o csv que mantém o histórico de dispositivos numa rede
        """
        firstRow = ['ID', 'IP', 'MAC', 'Fabricante', 'Hora Descoberta']
        with open('historico.csv', 'a') as h:
            writer = csv.writer(h)
            writer.writerow(firstRow)