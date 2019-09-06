import csv
class Writer():
    def __init__(self):
        pass

    def createCSV(self):
        """ Cria o csv que mantém o histórico de dispositivos numa rede
        """
        firstRow = ['ID', 'IP', 'MAC', 'Fabricante', 'Hora Descoberta']
        with open('historico.csv', 'a') as h:
            writer = csv.writer(h)
            writer.writerow(firstRow)