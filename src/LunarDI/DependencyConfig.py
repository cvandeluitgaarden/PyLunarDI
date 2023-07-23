from enum import Enum

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
    
    def impl_type(self, impl_type):
        self.instance_type = impl_type
        return self 

    def lifetime(self, lifetime:Lifetime):
        self.lifetime = lifetime
        return self
