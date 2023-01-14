import sys

sys.path.insert(0, "common")

from repo import Repo


class PrelicenseRepo(Repo):
    """
    A subclass of Repo that uses the /prelicenses subtree.
    """

    def __init__(self):
        """Creates a new PrelicenseRepo instance"""
        super().__init__(
            "prelicenses",
            ["name"],
            ["clientId"],
            ["name", "clientId", "product", "productVersion", "liberationCode"],
        )
