import sys
sys.path.insert(0, "domain")
from github_repo import GithubRepo
from incident_repo import IncidentRepo


class GithubIncidentRepo(IncidentRepo):
    """
    A IncidentRepo that uses Github as persistence backend
    """
    def __init__(self):
        super().__init__()
        self._githubRepo = GithubRepo(
            "incidents",
            self._entity_class.primary_key(),
            self._entity_class.filter_attributes(),
            self._entity_class.attributes())


    def path(self):
        """
        Retrieves the Github path.
        """
        return self._githubRepo.path


    def find_by_id(self, id):
        """
        Retrieves the Incident matching given id.
        """
        return self._githubRepo.find_by_id(id)


    def find_by_attribute(self, attribute_name, attribute_value):
        """
        Retrieves the Incident matching given attribute.
        """
        return self._githubRepo.find_by_attribute(attribute_name, attribute_value)


    def insert(self, item):
        """
        Inserts a new Incident
        """
        return self._githubRepo.insert(item)


    def update(self, item):
        """
        Updates a Incident
        """
        return self._githubRepo.update(item)


    def delete(self, id):
        """
        Deletes a Incident
        """
        return self._githubRepo.delete(id)


    def find_by_pk(self, pk):
        """
        Retrieves a Incident by its primary key
        """
        print(f"In github_incident_repo>>find_by_pk({pk})")
        return self._githubRepo.find_by_pk(pk)


    def list(self):
        """
        Lists all Incidents
        """
        return self._githubRepo.list()
