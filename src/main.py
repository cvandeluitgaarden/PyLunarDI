from Configuration import Config
from LunarDI.LunarDIContainer import LunarDIContainer
from Product.ProductServiceInterface import ProductServiceInterface

container = LunarDIContainer()
if __name__ == "__main__":
    Config.registerProductServices(container)
    impl = container.resolve(ProductServiceInterface)
    print(impl.getProduct("12"))



    
