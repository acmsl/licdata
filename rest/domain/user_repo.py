from repo import Repo
from user import User


class UserRepo(Repo):
    """
    A subclass of Repo that manages Users.
    """
    def __init__(self):
        """
        Creates a new UserRepo instance.
        """
        super().__init__(User)
