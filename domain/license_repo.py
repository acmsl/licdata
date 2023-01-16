from repo import Repo
import sys


class LicenseRepo(Repo):
    """
    A subclass of Repo that manages Licenses.
    """
    def __init__(self):
        """
        Creates a new LicenseRepo instance.
        """
        super().__init__(getattr(sys.modules[__name__], 'License'))
