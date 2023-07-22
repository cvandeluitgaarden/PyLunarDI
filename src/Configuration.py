from LunarDI.ContainerInterface import ContainerInterface
from Product.ProductRepository import ProductRepository
from Product.ProductRepositoryInterface import ProductRepositoryInterface
from Product.ProductService import ProductService
from Product.ProductServiceInterface import ProductServiceInterface


class Config:
    @staticmethod
    def registerProductServices(container:ContainerInterface):    
        container.addTransient(ProductRepositoryInterface, ProductRepository)
        container.addTransient(ProductServiceInterface, ProductService)