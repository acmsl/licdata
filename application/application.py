import sys

sys.path.insert(0, "infrastructure/github")
from githubclientrepo import GithubClientRepo

class Licdata():

    def __init__(self):
        pass

    @staticmethod
    def clientRepo():
        return GithubClientRepo()
