import random
from Connector import Connector
from ConnectorInterface import ConnectorInterface
from ExampleGui import ExampleGui
from LunarDI.LunarDIContainer import LunarDIContainer


container = LunarDIContainer()
if __name__ == "__main__":
    container.add_singleton(ConnectorInterface).type(Connector)
    container.add_transient(ExampleGui)
    
    guis = []
    for x in range(10):
        gui = container.resolve(ExampleGui)
        gui.name = "ExampleGui - {}".format(x)
        guis.append(gui)

    for x in range(20):
        i = random.randint(0, len(guis) - 1)
        p = random.randint(0, 1000)
        guis[i].open(p)
        guis[i].close()

        print("Connector opened connection {} times".format(guis[i].connector.open_count))
        print("----------------------------------------------------------")