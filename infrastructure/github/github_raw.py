import sys
sys.path.insert(0, "infrastructure")
from crypt_utils import encrypt, decrypt_file
from github_access import get_repo_and_branch


def get_contents(path):
    result = None

    (repo, branch) = get_repo_and_branch()

    file = repo.get_contents(path, ref=branch)

    try:
        result = decrypt_file(file, path)
    except Exception as e:
        result = None
        print(f"Cannot decrypt {path}: {e}")

    return (result, file.sha)


def create_file(path, content, message):
    result = None

    (repo, branch) = get_repo_and_branch()

    try:
        result = repo.create_file(
            path,
            message,
            encrypt(content),
            branch=branch,
        )
    except Exception as e:
        result = None
        print(f"Error creating file {path}: {e}")

    return result


def update_file(path, content, message, hash):
    result = None

    (repo, branch) = get_repo_and_branch()

    try:
        result = repo.update_file(
            path,
            message,
            encrypt(content),
            hash,
            branch=branch,
        )
    except Exception as e:
        result = None
        print(f"Error updating file {path}: {e}")

    return result


def delete_file(path, message):
    result = None

    (repo, branch) = get_repo_and_branch()

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
