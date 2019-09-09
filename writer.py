import csv
import os.path
import datetime
from device import Device
class Writer():
    def __init__(self):
        self.createCSV()
    def createCSV(self):
        """ Cria o csv que mantém o histórico de dispositivos numa rede
        """
        if (not os.path.exists('historico.csv')):
            firstRow = ['ID', 'IP', 'MAC', 'Fabricante', 'Hora Descoberta']
            with open('historico.csv', 'a') as h:
                writer = csv.writer(h)
                writer.writerow(firstRow)

    def writeToCSV(self, devices):
        now = datetime.datetime.now()
        with open('historico.csv', 'a') as h:
            writer = csv.writer(h)
            for device in devices:
                row = ['0', device.ip, device.mac, device.manufacturer, now.strftime("%x %Hh%mm")]
                writer.writerow(row)

    def getDevicesFromCSV(self):
        devices = []
        with open('historico.csv', 'r') as h:
            reader = csv.reader(h)
            for row in reader:
                devices.append(Device(ip = row[1], mac = row[2], manufacturer = row[3]))
        return devices