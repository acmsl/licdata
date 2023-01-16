from repo import Repo
import sys


class ProductRepo(Repo):
    """
    A subclass of Repo that manages Products.
    """
    def __init__(self):
        """
        Creates a new ProductRepo instance.
        """
        super().__init__(getattr(sys.modules[__name__], 'Product'))
