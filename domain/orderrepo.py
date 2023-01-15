import sys

sys.path.insert(0, "common")

from repo import Repo


class OrderRepo(Repo):
    """
    A subclass of Repo that uses the /orders subtree.
    """

    def __init__(self):
        """Creates a new OrderRepo instance"""
        super().__init__(
            "orders",
            [],
            ["clientId"],
            ["clientId", "product", "productVersion", "duration", "orderDate"],
        )
