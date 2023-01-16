from repo import Repo
from license import License


class LicenseRepo(Repo):
    """
    A subclass of Repo that manages Licenses.
    """
    def __init__(self):
        """
        Creates a new LicenseRepo instance.
        """
        super().__init__(License)
