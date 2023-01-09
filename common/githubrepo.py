from uuid import uuid4
import os
from github import Github


def getRepo():
    token = os.environ["GITHUB_TOKEN"]
    github = Github(token)
    repository = os.environ["GITHUB_REPO"]
    return github.get_repo(repository)


def getBranch():
    return os.environ["GITHUB_BRANCH"]


def newId():
    return str(uuid4())
