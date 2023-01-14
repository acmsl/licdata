import sys
sys.path.insert(0, "common")

from repo import Repo


class LicenseRepo(Repo):
    """
    A subclass of Repo that uses the /licenses subtree.
    """
    def __init__(self):
        """Creates a new LicenseRepo instance"""
        super().__init__(
            "licenses",
            [""],
            ["clientId"],
            ["clientId", "product", "productVersion"],
        )
