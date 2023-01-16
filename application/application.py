import sys
sys.path.insert(0, "infrastructure/github")
from github_client_repo import GithubClientRepo


class Licdata():

    def __init__(self):
        pass

    @staticmethod
    def clientRepo():
        return GithubClientRepo()
