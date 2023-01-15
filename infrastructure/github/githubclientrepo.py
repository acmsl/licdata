import sys
sys.path.insert(0, "domain")
from githubrepo import GithubRepo
from clientrepo import ClientRepo

class GithubClientRepo(ClientRepo):
    """
    A ClientRepo that uses Github as persistence backend
    """
    def __init__(self):
        super().__init__()
        self._githubRepo = GithubRepo("clients", self.entityClass().primaryKey(), self.entityClass().filterAttributes(), self.entityClass().attributes())


    def findById(self, id):
        return self._githubRepo.findById(id)


    def findByAttribute(self, attributeName, attributeValue):
        return self._githubRepo.findByAttribute(attributeName, attributeValue)


    def insert(self, item):
        return self._githubRepo.insert(item)


    def update(self, item):
        return self._githubRepo.update(item)


    def delete(self, id):
        return self._githubRepo.delete(item)


    def findByPk(self, pk):
        return self._githubRepo.findByPk(item)


    def list(self):
        return self._githubRepo.list(item)
