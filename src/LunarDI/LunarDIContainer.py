
from enum import Enum
import importlib
import inspect

from LunarDI.ContainerInterface import ContainerInterface

class DIType(Enum):
    SINGLETON = 0
    TRANSIENT = 1
    

class LunarDIContainer(ContainerInterface):

    IMPL_TYPE = "IT"
    TYPE = "T"

    container = {}
    impls = {}

    def __init__(self):
        self.addSingleton(ContainerInterface, self)

    def addTransient(self, type1, type2):
        self.container.update({type1 : { self.IMPL_TYPE: type2, self.TYPE : DIType.TRANSIENT }})
        return self

    def addSingleton(self, type1, type2):
        self.container.update({type1 : { self.IMPL_TYPE: type2, self.TYPE : DIType.SINGLETON }})
        self.impls.update({ type1 : type2 })
        return self


    def get_args(self, c):
        args = inspect.getfullargspec(c.__init__)
        classes = []
        for t in args.annotations:
            classes.append(self.resolve(args.annotations[t]))
            
        return classes

    def resolve(self, t):
        implType = self.container[t]

        match implType[self.TYPE]:
            case DIType.SINGLETON:
                if not implType[self.IMPL_TYPE] in self.impls:
                    self.impls.update({ implType[self.IMPL_TYPE] : self.createInst(implType) })

                return self.impls[implType[self.IMPL_TYPE]]
            case _:
                return self.createInst(implType)
    
    def createInst(self, type1):
        segments = type1[self.IMPL_TYPE].__module__.split(".")
        module = importlib.import_module(type1[self.IMPL_TYPE].__module__)
        class_ = getattr(module, segments[-1])
        args = self.get_args(class_)
        
        if(len(args) > 0): 
            return class_(*args) 
        else: 
            return class_()
