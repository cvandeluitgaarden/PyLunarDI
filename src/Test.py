from Product.ProductService import ProductService
from Product.ProductServiceInterface import ProductServiceInterface

class Test:
    def __init__(self, service: ProductService):
        self.service = service

    def pr(self):
        print(self.service.__dict__)
        self.service.get_product(12)

