import os
import threading
from github import Github


def getRepo():
    local = threading.local()

    if not hasattr(local, "repo"):
        if not hasattr(local, "token"):
            local.token = os.environ["GITHUB_TOKEN"]

        if not hasattr(local, "github"):
            local.github = Github(local.token)

        if not hasattr(local, "repositoryName"):
            local.repositoryName = os.environ["GITHUB_REPO"]

        local.repo = local.github.get_repo(local.repositoryName)

    return local.repo


def getBranch():
    local = threading.local()

    if not hasattr(local, "branch"):
        local.branch = os.environ["GITHUB_BRANCH"]

    return local.branch


def getRepoAndBranch():
    return (getRepo(), getBranch())
