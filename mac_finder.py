class Macfinder:
    def __init__(self, MAC):
        self.MAC = MAC
        self.manufacturer = self.parseManuf()

    def parseManuf(self):
        """ Trata o arquivo Manuf e retorna um dicionário com
        o MAC e seu fabricante

        Returns:
            Object -- Dicionário contendo MAC e nome do fabricante
        """
        d = {}
        with open("manuf") as f:
            for line in f:
                line_parsed = line.split("\t", 1)
                if (line[0] is not '#' and len(line_parsed) > 1):
                    (key, val) = line_parsed
                    d[key] = val
        return d
