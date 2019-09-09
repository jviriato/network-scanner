class Device:
    def __init__(self, ip, mac, manufacturer, isHost = True):
        self.ip = ip
        self.mac = mac
        self.manufacturer = manufacturer
        self.isHost = isHost

    def __repr__(self):
        return '\nIP:    {}\nMAC:   {}\nManuf: {}\n'.format(
        self.ip,
        self.mac,
        self.manufacturer
        )