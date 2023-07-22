from Product.ProductRepositoryInterface import ProductRepositoryInterface
from Product.ProductServiceInterface import ProductServiceInterface


class ProductService(ProductServiceInterface):

    def __init__(self, repository: ProductRepositoryInterface):
        self.repository = repository

    def getProduct(self, productNumber:str):
        return self.repository.getProducts([ productNumber ])