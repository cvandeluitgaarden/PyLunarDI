from Connector import ConnectorInterface

class ExampleGui:

    def __init__(self, connector:ConnectorInterface):
        self.connector = connector
        self.name = "ExampleGuid"

    def open(self, port):
        print("{}: open({})".format(self.name, port))
        self.connector.open(port)
    
    def close(self):
        print("{}: close()".format(self.name))
        self.connector.close()