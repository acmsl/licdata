import sys
sys.path.insert(0, "common")

from repo import Repo


class PcRepo(Repo):
    """
    A subclass of Repo that uses the /pcs subtree.
    """
    def __init__(self):
        """Creates a new PcRepo instance"""
        super().__init__(
            "pcs",
            ["email"],
            ["email"],
            ["email", "address", "contact", "phone"],
        )
