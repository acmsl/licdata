def getRepo():
    local = threading.local()

    if not local.repo:
        if not local.token:
            local.token = os.environ["GITHUB_TOKEN"]

        if not local.github:
            local.github = Github(local.token)

        if not local.repositoryName:
            local.repositoryName = os.environ["GITHUB_REPO"]

        local.repo = local.github.get_repo(local.repositoryName)

    return local.repo


def getBranch():
    if not local.branch:
        local.branch = os.environ["GITHUB_BRANCH"]

    return local.branch


def getRepoAndBranch():
    return (getRepo(), getBranch())
