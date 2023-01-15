import sys

sys.path.insert(0, "common")

from repo import Repo


class ProductRepo(Repo):
    """
    A subclass of Repo that uses the /products subtree.
    """

    def __init__(self):
        """Creates a new ProductRepo instance"""
        super().__init__(
            "products",
            ["name"],
            ["name"],
            ["name", "productTypeId", "productVersion"],
        )
