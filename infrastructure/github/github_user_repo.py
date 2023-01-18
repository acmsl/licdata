import sys

sys.path.insert(0, "domain")
from github_repo import GithubRepo
from user_repo import UserRepo


class GithubUserRepo(UserRepo):
    """
    A UserRepo that uses Github as persistence backend
    """
    def __init__(self):
        super().__init__()
        self._githubRepo = GithubRepo("users", self._entity_class)

    def path(self):
        """
        Retrieves the Github path.
        """
        return self._githubRepo.path

    def find_by_id(self, id):
        """
        Retrieves the User matching given id.
        """
        return self._githubRepo.find_by_id(id)

    def find_by_attribute(self, attribute_name, attribute_value):
        """
        Retrieves the User matching given attribute.
        """
        return self._githubRepo.find_by_attribute(attribute_name, attribute_value)

    def insert(self, item):
        """
        Inserts a new User
        """
        return self._githubRepo.insert(item)

    def update(self, item):
        """
        Updates an User
        """
        return self._githubRepo.update(item)

    def delete(self, id):
        """
        Deletes an User
        """
        return self._githubRepo.delete(id)

    def find_by_pk(self, pk):
        """
        Retrieves an User by its primary key
        """
        return self._githubRepo.find_by_pk(pk)

    def list(self):
        """
        Lists all users
        """
        return self._githubRepo.list()
