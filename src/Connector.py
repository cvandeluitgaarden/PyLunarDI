from enum import Enum
from ConnectorInterface import ConnectorInterface

class Connector(ConnectorInterface):

    open_count = 0
    close_count = 0

    def __init__(self):
        self.connection_status = ConnectionStatus.Closed

    def open(self, port):
        if self.connection_status != ConnectionStatus.Closed:
            print("Connection already open")    
        
        self.open_count += 1
        self.port = port
        self.connection_status = ConnectionStatus.Open
        print("Opened connection on port {}".format(self.port))

    def close(self):
        if self.connection_status == ConnectionStatus.Open:
            self.close_count += 1
            self.connection_status = ConnectionStatus.Closed
            print("Closed connection on port {}".format(self.port))

class ConnectionStatus(Enum):
    Closed = 0
    Open = 1