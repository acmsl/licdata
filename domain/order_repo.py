from repo import Repo
import sys


class OrderRepo(Repo):
    """
    A subclass of Repo that manages Orders.
    """
    def __init__(self):
        """
        Creates a new OrderRepo instance.
        """
        super().__init__(getattr(sys.modules[__name__], 'Order'))
