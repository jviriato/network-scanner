
import subprocess
import csv
from mac_finder import MacFinder
from device import Device
from datetime import date
class NetworkScanner:
    """ Classe para realizar o scan da rede.
    """
    def __init__(self):
        self.today = date.today()
