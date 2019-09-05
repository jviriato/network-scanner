class MacFinder:
    """ Classe para tratar casos relacionados ao endereço MAC.

    """
    def __init__(self, mac):
        """ Inicializa o objeto.

        Arguments:
            mac {str} -- O endereço MAC do dispositivo.
        """
        self.mac = mac
        self.manuf = self.parseManuf()

    def parseManuf(self):
        """ Trata o arquivo Manuf e retorna um dicionário com
        o MAC e seu fabricante.

        Returns:
            Object -- Dicionário contendo MAC e nome do fabricante.
        """
        d = {}
        with open("manuf") as f:                            #win: with open("manuf.txt", encoding='utf-8') as f:
            for line in f:
                line_parsed = line.split("\t", 1)
                if (line[0] != '#' and len(line_parsed) > 1):
                    (key, val) = line_parsed
                    d[key] = val
        return d

    def getManufacturer(self):
        """Retorna o Fabricante à partir de um endereço MAC.
        """
        self.mac.replace('-', ':')
        initMac = self.mac[0:8].upper()
        d = self.parseManuf()

        fabricante = d.get(initMac, 'Este MAC não existe!')
        return fabricante
