class MacFinder:
    """ Classe para tratar casos relacionados ao endereço MAC.

    """
    def __init__(self):
        """ Inicializa o objeto.
        """
        self.manuf = self.parseManuf()

    def parseManuf(self):
        """ Trata o arquivo Manuf e retorna um dicionário com
        o MAC e seu fabricante.

        Returns:
            Object -- Dicionário contendo MAC e nome do fabricante.
        """
        d = {}
        with open("manuf.txt", encoding='utf-8') as f:
            for line in f:
                line_parsed = line.split("\t", 1)
                if (line[0] != '#' and len(line_parsed) > 1):
                    (key, val) = line_parsed
                    d[key] = val.rstrip('\n')
        return d


    def _parseMACManufacturer(self, mac):
      """ Retorna os 3 primeiros sets do endereço MAC.
      """
      return mac.replace('-', ':')[:8].upper()

    def getManufacturer(self, mac):
        """Retorna o Fabricante à partir de um endereço MAC.
        """
        initMac = self._parseMACManufacturer(mac)
        return self.manuf.get(initMac, 'Não consegui identificar o criador')
    