from Product.ProductRepositoryInterface import ProductRepositoryInterface

class ProductRepository(ProductRepositoryInterface):
    def get_products(self, productNumbers : list[str]):
        return " " .join(productNumbers)