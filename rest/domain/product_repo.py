from repo import Repo
from product import Product


class ProductRepo(Repo):
    """
    A subclass of Repo that manages Products.
    """
    def __init__(self):
        """
        Creates a new ProductRepo instance.
        """
        super().__init__(Product)
