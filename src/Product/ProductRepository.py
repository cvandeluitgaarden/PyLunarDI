from Product.ProductRepositoryInterface import ProductRepositoryInterface

class ProductRepository(ProductRepositoryInterface):
    def getProducts(self, productNumbers : list[str]):
        return " " .join(productNumbers)