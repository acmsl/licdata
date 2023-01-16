from repo import Repo
import sys


class IncidentRepo(Repo):
    """
    A subclass of Repo that manages Incidents.
    """
    def __init__(self):
        """
        Creates a new IncidentRepo instance.
        """
        super().__init__(getattr(sys.modules[__name__], 'Incident'))
