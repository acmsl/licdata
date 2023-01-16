from repo import Repo
from order import Order


class OrderRepo(Repo):
    """
    A subclass of Repo that manages Orders.
    """
    def __init__(self):
        """
        Creates a new OrderRepo instance.
        """
        super().__init__(Order)
