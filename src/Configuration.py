from LunarDI.ContainerInterface import ContainerInterface
from Product.ProductRepository import ProductRepository
from Product.ProductRepositoryInterface import ProductRepositoryInterface
from Product.ProductService import ProductService
from Product.ProductServiceInterface import ProductServiceInterface

class Config:
    @staticmethod
    def add_product_feature(container:ContainerInterface):
        container.add_singleton(ProductRepositoryInterface).factory(Config.factory_method)
        container.add_transient(ProductServiceInterface).impl_type(ProductService)

    @staticmethod
    def factory_method():
        return ProductRepository("TEST")

    

