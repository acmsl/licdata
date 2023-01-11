import githubaccess
import crypt


def getContents(path):
    result = None

    (repo, branch) = githubaccess.getRepoAndBranch()

    try:
        result = crypt.decryptFile(repo.get_contents(path, ref=branch), path)
    except:
        result = None

    return result


def createFile(path, content, message):
    result = None

    (repo, branch) = githubaccess.getRepoAndBranch()

    try:
        result = repo.create_file(
            path,
            message,
            crypt.encrypt(content),
            branch=branch,
        )
    except:
        result = None

    return result


def updateFile(path, content, hash, message):
    result = None

    (repo, branch) = githubaccess.getRepoAndBranch()

    try:
        result = repo.update_file(
            path,
            message,
            crypt.encrypt(content),
            hash,
            branch=branch,
        )
    except:
        result = None

    return result


def deleteFile(path, hash, message):
    result = None

    (repo, branch) = githubaccess.getRepoAndBranch()

    try:
        result = repo.delete_file(
            path,
            message,
            hash,
            branch=branch,
        )
    except:
        result = None

    return result
