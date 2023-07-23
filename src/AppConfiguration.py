from LunarDI.LunarDIContainer import ContainerInterface
from Connector import *
from ExampleGui import ExampleGui
from App import App
from Dictionary import *
import time
from Bot import *

class AppConfiguration:

    def configure(self, container:ContainerInterface, language):
        self.container = container
        container.add_singleton(ConnectorInterface).type(LoveConnector)
        container.add_transient(ExampleGui)
        container.add_transient(App)
        container.add_singleton(DictionaryInterface).impl(self.get_dictionary(language))

        container.add_transient(AfternoonBot)
        container.add_transient(MorningBot)
        container.add_transient(NightBot)
        container.add_transient(BotInterface).factory(self.get_bot)

    def get_bot(self):
        t = time.localtime() 
        if t.tm_hour >= 6 and t.tm_hour < 12:
            return self.container.resolve(MorningBot)
        elif t.tm_hour >= 12 and t.tm_hour < 18:
            return self.container.resolve(AfternoonBot)
        else:
            return self.container.resolve(NightBot)
    
    def get_dictionary(self, language):
        match language:
            case "NL":
                return DictionaryNL()
            case "EN":
                return DictionaryEN()
            case "DE": 
                return DictionaryDE()
            case "TR":
                return DictionaryTR()
