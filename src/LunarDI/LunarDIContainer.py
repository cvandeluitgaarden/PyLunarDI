
import importlib
import inspect

from LunarDI.ContainerInterface import ContainerInterface

class LunarDIContainer(ContainerInterface):

    container = {}

    def __init__(self):
        pass

    def addTransient(self, type1, type2):
        self.container.update({ type1: type2 })
        return self

    def get_args(self, c):
        args = inspect.getfullargspec(c.__init__)
        classes = []
        for t in args.annotations:
            classes.append(self.resolve(args.annotations[t]))
            
        return classes

    def resolve(self, t):
        implType = self.container[t]
        segments = implType.__module__.split(".")
        module = importlib.import_module(implType.__module__)
        class_ = getattr(module, segments[-1])
        args = self.get_args(class_)
        
        if(len(args) > 0): 
            return class_(*args) 
        else: 
            return class_()
    