from repo import Repo
from product_type import ProductType


class ProductTypeRepo(Repo):
    """
    A subclass of Repo that manages ProductTypes.
    """
    def __init__(self):
        """
        Creates a new ProductTypeRepo instance.
        """
        super().__init__(ProductType)
