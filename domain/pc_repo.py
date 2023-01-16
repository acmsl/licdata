from repo import Repo
import sys


class PcRepo(Repo):
    """
    A subclass of Repo that manages PCs.
    """
    def __init__(self):
        """
        Creates a new PcRepo instance.
        """
        super().__init__(getattr(sys.modules[__name__], 'Pc'))
