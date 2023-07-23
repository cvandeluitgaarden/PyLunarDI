from Configuration import Config
from LunarDI.LunarDIContainer import LunarDIContainer
from Product.ProductServiceInterface import ProductServiceInterface

container = LunarDIContainer()
if __name__ == "__main__":
    Config.add_product_feature(container)
    impl = container.resolve(ProductServiceInterface)
    print(impl.get_product("12"))




