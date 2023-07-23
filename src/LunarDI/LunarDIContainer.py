from enum import Enum
import importlib
import inspect

class Lifetime(Enum):
    NONE = 0
    SINGLETON = 1
    TRANSIENT = 2

class DependencyConfig:

    factory_method = None
    instance = None

    def __init__(self, t1, t2):
        self.declaration_type = t1
        self.instance_type = t2

    def factory(self, factory_method):
        self.factory_method = factory_method
        return self

    def impl(self, instance):
        self.instance = instance
        return self
    
    def type(self, impl_type):
        self.instance_type = impl_type
        return self 

    def lifetime(self, lifetime:Lifetime):
        self.lifetime = lifetime
        return self

class ContainerInterface:
    def add_transient(self, t1) -> DependencyConfig:
        pass

    def add_singleton(self, t1) -> DependencyConfig:
        pass

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
        clss = getattr(module, config.instance_type.__name__)
        args = self.get_args(clss)
        
        if(len(args) > 0): 
            return clss(*args) 
        else: 
            return clss()