class ConnectorInterface:
    def open(self, port:int) -> bool:
        pass

    def close(self) -> bool:
        pass