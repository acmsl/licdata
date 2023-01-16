from repo import Repo
from client import Client


class ClientRepo(Repo):
    """
    A subclass of Repo that manages Clients.
    """
    def __init__(self):
        """
        Creates a new ClientRepo instance.
        """
        super().__init__(Client)
