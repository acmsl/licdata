import sys

sys.path.insert(0, "common")

from repo import Repo


class ProductTypeRepo(Repo):
    """
    A subclass of Repo that uses the /producttypes subtree.
    """

    def __init__(self):
        """Creates a new ProductTypeRepo instance"""
        super().__init__(
            "producttypes",
            ["name"],
            ["name"],
            ["name"],
        )
