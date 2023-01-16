import sys
sys.path.insert(0, "domain")
from github_repo import GithubRepo
from client_repo import ClientRepo

class GithubClientRepo(ClientRepo):
    """
    A ClientRepo that uses Github as persistence backend
    """
    def __init__(self):
        super().__init__()
        self._githubRepo = GithubRepo(
            "clients",
            self._entity_class.primary_key(),
            self._entity_class.filter_attributes(),
            self._entity_class.attributes())


    def find_by_id(self, id):
        return self._githubRepo.find_by_id(id)


    def find_by_attribute(self, attribute_name, attribute_value):
        return self._githubRepo.find_by_attribute(attribute_name, attribute_value)


    def insert(self, item):
        return self._githubRepo.insert(item)


    def update(self, item):
        return self._githubRepo.update(item)


    def delete(self, id):
        return self._githubRepo.delete(id)


    def find_by_pk(self, pk):
        return self._githubRepo.find_by_pk(pk)


    def list(self):
        return self._githubRepo.list()
