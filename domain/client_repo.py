from repo import Repo
import sys


class ClientRepo(Repo):
    """
    A subclass of Repo that manages Clients.
    """
    def __init__(self):
        """
        Creates a new ClientRepo instance.
        """
        super().__init__(getattr(sys.modules[__name__], 'Client'))
