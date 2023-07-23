from abc import abstractmethod
from Dictionary import DictionaryInterface

class BotInterface:
    def greet(self) -> str:
        pass

@abstractmethod
class AbstractBot(BotInterface):
    def __init__(self, dictionary:DictionaryInterface):
        self.dictionary = dictionary

class MorningBot(AbstractBot):
    def greet(self):
        return self.dictionary.GOOD_MORNING

class AfternoonBot(AbstractBot):
    def greet(self):
        return self.dictionary.GOOD_AFTERNOON

class NightBot(AbstractBot):
    def greet(self):
        return self.dictionary.GOOD_NIGHT

