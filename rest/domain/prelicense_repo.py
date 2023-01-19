from repo import Repo
from prelicense import Prelicense


class PrelicenseRepo(Repo):
    """
    A subclass of Repo that manages Prelicenses.
    """
    def __init__(self):
        """
        Creates a new Prelicense instance.
        """
        super().__init__(Prelicense)
