
from enum import Enum
import importlib
import inspect

from LunarDI.ContainerInterface import ContainerInterface

class Lifetime(Enum):
    SINGLETON = 0
    TRANSIENT = 1
    

class LunarDIContainer(ContainerInterface):

    IMPL_TYPE = "IT"
    TYPE = "T"

    container = {}
    impls = {}

    def __init__(self):
        self.add_singleton(ContainerInterface, self)

    def add_transient(self, t1, t2):
        self.container.update({t1 : { self.IMPL_TYPE: t2, self.TYPE : Lifetime.TRANSIENT }})
        return self

    def add_singleton(self, t1, t2):
        self.container.update({t1 : { self.IMPL_TYPE: t2, self.TYPE : Lifetime.SINGLETON }})
        self.impls.update({ t1 : t2 })
        return self


    def get_args(self, c):
        args = inspect.getfullargspec(c.__init__)
        classes = []
        for t in args.annotations:
            classes.append(self.resolve(args.annotations[t]))
            
        return classes

    def resolve(self, t):
        impl_type = self.container[t]

        match impl_type[self.TYPE]:
            case Lifetime.SINGLETON:
                if not impl_type[self.IMPL_TYPE] in self.impls:
                    self.impls.update({ impl_type[self.IMPL_TYPE] : self.create_impl(impl_type) })

                return self.impls[impl_type[self.IMPL_TYPE]]
            case _:
                return self.create_impl(impl_type)
    
    def create_impl(self, t):
        segments = t[self.IMPL_TYPE].__module__.split(".")
        m = importlib.import_module(t[self.IMPL_TYPE].__module__)
        c = getattr(m, segments[-1])
        args = self.get_args(c)
        
        if(len(args) > 0): 
            return c(*args) 
        else: 
            return c()
