class Device:
    def __init__(self, ip, mac, manufacturer, isHost = True, status = "Offline"):
        self.ip = ip
        self.mac = mac
        self.manufacturer = manufacturer
        self.isHost = isHost
        self.status = status

    def __repr__(self):
        return '\nIP:      {}\nMAC:     {}\nManuf:   {}\nStatus:  {}\n'.format(
        self.ip,
        self.mac,
        self.manufacturer,
        self.status
        )
    
    def __eq__(self, another):
        return self.mac == another.mac
    
    def __hash__(self):
        return hash(('mac', self.mac))