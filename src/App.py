
import random
from Bot import BotInterface
from ExampleGui import ExampleGui
from LunarDI.LunarDIContainer import ContainerInterface

class App():
    def __init__(self, container:ContainerInterface, bot:BotInterface):
        self.container = container
        self.bot = bot

    def run(self):

        print("--- " + self.bot.greet() + " ---")

        guis = []
        for x in range(10):
            gui = self.container.resolve(ExampleGui)
            gui.name = "ExampleGui - {}".format(x)
            guis.append(gui)

        for x in range(20):
            i = random.randint(0, len(guis) - 1)
            p = random.randint(0, 1000)
            guis[i].open(p)
            guis[i].close()

            print("Connector opened connection {} times".format(guis[i].connector.open_count))
            print("----------------------------------------------------------")