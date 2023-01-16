from repo import Repo
from pc import Pc


class PcRepo(Repo):
    """
    A subclass of Repo that manages PCs.
    """
    def __init__(self):
        """
        Creates a new PcRepo instance.
        """
        super().__init__(Pc)
