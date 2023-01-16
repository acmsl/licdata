import os
import threading
from github import Github


def get_repo():
    local = threading.local()

    if not hasattr(local, "repo"):
        if not hasattr(local, "token"):
            local.token = os.environ["GITHUB_TOKEN"]

        if not hasattr(local, "github"):
            local.github = Github(local.token)

        if not hasattr(local, "repository_name"):
            local.repository_name = os.environ["GITHUB_REPO"]

        local.repo = local.github.get_repo(local.repository_name)

    return local.repo

def get_branch():
    local = threading.local()

    if not hasattr(local, "branch"):
        local.branch = os.environ["GITHUB_BRANCH"]

    return local.branch


def get_repo_and_branch():
    return (get_repo(), get_branch())
