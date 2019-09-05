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
        with open("manuf") as f:
            for line in f:
                line_parsed = line.split("\t", 1)
                if (line[0] != '#' and len(line_parsed) > 1):
                    (key, val) = line_parsed
                    d[key] = val
        return d

    def _parseMACManufacturer(self):
      """ Retorna os 3 primeiros sets do endereço MAC.
      """
      return self.mac.replace('-', ':')[:8]

    def getManufacturer(self):
        """Retorna o Fabricante à partir de um endereço MAC.
        
        Arguments:
            mac {str} -- Endereço MAC
        """
        macManuf = self._parseMACManufacturer()
        return self.manuf[macManuf]
