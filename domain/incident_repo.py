from repo import Repo
from incident import Incident


class IncidentRepo(Repo):
    """
    A subclass of Repo that manages Incidents.
    """
    def __init__(self):
        """
        Creates a new IncidentRepo instance.
        """
        super().__init__(Incident)
