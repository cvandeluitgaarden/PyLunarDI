from enum import Enum
from Dictionary import DictionaryInterface

class ConnectorInterface:
    def open(self, port:int) -> bool:
        pass

    def close(self) -> bool:
        pass

class ConnectionStatus(Enum):
    Closed = 0
    Open = 1

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

class LoveConnector(ConnectorInterface):

    open_count = 0
    close_count = 0

    def __init__(self, dictionary:DictionaryInterface):
        self.connection_status = ConnectionStatus.Closed
        print(dictionary.HEART)

    def open(self, port):

        if self.connection_status != ConnectionStatus.Closed:
            print("Infinite love connection opened")
        
        self.open_count += 1
        self.port = port
        self.connection_status = ConnectionStatus.Open

    def close(self):
        if self.connection_status == ConnectionStatus.Open:
            print("Infinite love connection can't be closed")


