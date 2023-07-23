from LunarDI.ContainerInterface import ContainerInterface
from Product.ProductRepository import ProductRepository
from Product.ProductRepositoryInterface import ProductRepositoryInterface
from Product.ProductService import ProductService
from Product.ProductServiceInterface import ProductServiceInterface


class Config:
    @staticmethod
    def add_product_feature(container:ContainerInterface):    
        container.add_transient(ProductRepositoryInterface, ProductRepository)
        container.add_transient(ProductServiceInterface, ProductService)