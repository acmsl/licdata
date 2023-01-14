import sys
sys.path.insert(0, "common")

from repo import Repo


class IncidentRepo(Repo):
    """
    A subclass of Repo that uses the /incidents subtree.
    """
    def __init__(self):
        """Creates a new IncidentRepo instance"""
        super().__init__(
            "incidents",
            [""],
            ["email"],
            ["product", "productVersion", "installationCode"],
        )
