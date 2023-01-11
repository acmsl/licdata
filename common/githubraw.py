import githubaccess
import crypt


def getContents(path):
    result = None

    (repo, branch) = githubaccess.getRepoAndBranch()

    file = repo.get_contents(path, ref=branch)

    try:
        result = crypt.decryptFile(file, path)
    except Exception as e:
        result = None
        print(f"Cannot decrypt {path}: {e}")

    return (result, file.sha)


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
    except Exception as e:
        result = None
        print(f"Error creating file {path}: {e}")

    return result


def updateFile(path, content, message, hash):
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
    except Exception as e:
        result = None
        print(f"Error updating file {path}: {e}")

    return result


def deleteFile(path, message):
    result = None

    (repo, branch) = githubaccess.getRepoAndBranch()

    try:
        (result, hash) = getContents(path)

        result = repo.delete_file(
            path,
            message,
            hash,
            branch=branch,
        )
    except Exception as e:
        result = None
        print(f"Error deleting file {path}: {e}")

    return result
