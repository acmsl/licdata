from repo import Repo
from client import Client
import sys

class ClientRepo(Repo):
    """
    A subclass of Repo that uses the /clients subtree.
    """
    def __init__(self):
        """Creates a new ClientRepo instance"""
        super().__init__(getattr(sys.modules[__name__],'Client'))
