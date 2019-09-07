import csv
import os.path
import datetime
from device import Device
class Writer():
    def __init__(self, devices):
        self.createCSV()
        self.devices = devices
    def createCSV(self):
        """ Cria o csv que mantém o histórico de dispositivos numa rede
        """
        if (not os.path.exists('historico.csv')):
            firstRow = ['ID', 'IP', 'MAC', 'Fabricante', 'Hora Descoberta']
            with open('historico.csv', 'a') as h:
                writer = csv.writer(h)
                writer.writerow(firstRow)

    def writeToCSV(self):
        now = datetime.datetime.now()
        with open('historico.csv', 'a') as h:
            writer = csv.writer(h)
            for device in self.devices:
                row = ['0', device.ip, device.mac, device.manufacturer, now.strftime("%D %Hh%mm")]
                writer.writerow(row)
