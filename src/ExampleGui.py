from ConnectorInterface import ConnectorInterface

class ExampleGui:

    def __init__(self, connector:ConnectorInterface):
        self.connector = connector
        self.name = "ExampleGuid"

    def open(self, port):
        print("{0}: open({0})".format(self.name, port))
        self.connector.open(port)
    
    def close(self):
        print("{0}: close()".format(self.name))
        self.connector.close()