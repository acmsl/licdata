from repo import Repo
import sys


class ProductTypeRepo(Repo):
    """
    A subclass of Repo that manages ProductTypes.
    """
    def __init__(self):
        """
        Creates a new ProductTypeRepo instance.
        """
        super().__init__(getattr(sys.modules[__name__], 'ProductType'))
