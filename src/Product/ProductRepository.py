from Product.ProductRepositoryInterface import ProductRepositoryInterface

class ProductRepository(ProductRepositoryInterface):

    def __init__(self, t:str):
        self.t = t

    def get_products(self, productNumbers : list[str]):
        return " " .join(productNumbers) + self.t