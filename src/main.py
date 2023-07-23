from AppConfiguration import AppConfiguration
from LunarDI.LunarDIContainer import LunarDIContainer
from App import App

container = LunarDIContainer()
if __name__ == "__main__":
    AppConfiguration().configure(container, "TR")
    container.resolve(App).run()