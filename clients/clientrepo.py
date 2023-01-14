import sys
sys.path.insert(0, "common")

from repo import Repo


class ClientRepo(Repo):
    """
    A subclass of Repo that uses the /clients subtree.
    """
    def __init__(self):
        """Creates a new ClientRepo instance"""
        super().__init__(
            "clients",
            ["email"],
            ["email"],
            ["email", "address", "contact", "phone"],
        )
