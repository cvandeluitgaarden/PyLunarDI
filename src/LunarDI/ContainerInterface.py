from LunarDI.DependencyConfig import DependencyConfig


class ContainerInterface:
    def add_transient(self, t1) -> DependencyConfig:
        pass

    def add_singleton(self, t1) -> DependencyConfig:
        pass