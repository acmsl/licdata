import sys
sys.path.insert(0, "domain")
from github_repo import GithubRepo
from prelicense_repo import PrelicenseRepo


class GithubPrelicenseRepo(PrelicenseRepo):
    """
    A PrelicenseRepo that uses Github as persistence backend
    """
    def __init__(self):
        super().__init__()
        self._githubRepo = GithubRepo("prelicenses", self._entity_class)


    def path(self):
        """
        Retrieves the Github path.
        """
        return self._githubRepo.path


    def find_by_id(self, id):
        """
        Retrieves the Prelicense matching given id.
        """
        return self._githubRepo.find_by_id(id)


    def find_by_attribute(self, attribute_name, attribute_value):
        """
        Retrieves the Prelicense matching given attribute.
        """
        return self._githubRepo.find_by_attribute(attribute_name, attribute_value)


    def insert(self, item):
        """
        Inserts a new Prelicense
        """
        return self._githubRepo.insert(item)


    def update(self, item):
        """
        Updates a Prelicense
        """
        return self._githubRepo.update(item)


    def delete(self, id):
        """
        Deletes a Prelicense
        """
        return self._githubRepo.delete(id)


    def find_by_pk(self, pk):
        """
        Retrieves a Prelicense by its primary key
        """
        return self._githubRepo.find_by_pk(pk)


    def list(self):
        """
        Lists all Prelicenses
        """
        return self._githubRepo.list()
