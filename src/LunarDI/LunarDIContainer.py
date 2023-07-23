import importlib
import inspect

from LunarDI.ContainerInterface import ContainerInterface
from LunarDI.DependencyConfig import DependencyConfig, Lifetime

class LunarDIContainer(ContainerInterface):

    CONFIG = "C"
    container = {}

    def __init__(self):
        config = self.add_singleton(ContainerInterface).impl(self)
        
    def add_transient(self, t1) -> DependencyConfig:
        return self._add_transient(t1, t1)

    def _add_transient(self, t1, t2) -> DependencyConfig:
        config = DependencyConfig(t1, t2).lifetime(Lifetime.TRANSIENT)
        self.container.update({ t1 : { self.CONFIG : config } })
        return config

    def add_singleton(self, t1) -> DependencyConfig:
        return self._add_singleton(t1, t1)

    def _add_singleton(self, t1, t2) -> DependencyConfig:
        config = DependencyConfig(t1, t2).lifetime(Lifetime.SINGLETON)
        self.container.update({t1 : { self.CONFIG : config }})
        return config

    def get_args(self, c):
        args = inspect.getfullargspec(c.__init__)
        classes = []
        for t in args.annotations:
            classes.append(self.resolve(args.annotations[t]))
            
        return classes

    def resolve(self, t):
        config = self.container[t][self.CONFIG]
        match config.lifetime:
            case Lifetime.SINGLETON:
                if not config.instance is None:
                    return config.instance

                if not config.factory_method is None:
                    config.instance = config.factory_method()
                else:
                    config.instance = self.create_impl(config)
                
                return config.instance
            case _:
                if not config.factory_method is None:
                    return config.factory_method()
                else:
                    return self.create_impl(config)
    
    def create_impl(self, config:DependencyConfig):
        segments = config.instance_type.__module__.split(".")
        module = importlib.import_module(config.instance_type.__module__)
        clss = getattr(module, segments[-1])
        args = self.get_args(clss)
        
        if(len(args) > 0): 
            return clss(*args) 
        else: 
            return clss()
