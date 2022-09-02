import json
from uuid import uuid4
import os
from github import Github


def findById(id):
    token = os.environ["GITHUB_TOKEN"]
    github = Github(token)
    repository = os.environ["GITHUB_REPO"]
    repo = github.get_repo(repository)
    branch = os.environ["GITHUB_BRANCH"]
    incident = None
    try:
        file = repo.get_contents(f"incidents/{id}/data.json", ref=branch)
    except:
        file = None
    if file:
        incident = json.loads(file.decoded_content.decode())
    return incident


def insert(licenseId, email, product, productVersion, installationCode):
    token = os.environ["GITHUB_TOKEN"]
    github = Github(token)
    repository = os.environ["GITHUB_REPO"]
    repo = github.get_repo(repository)
    branch = os.environ["GITHUB_BRANCH"]
    result = str(uuid4())

    item = {}
    item["id"] = result
    item["licenseId"] = licenseId
    item["email"] = email
    item["product"] = product
    item["productVersion"] = productVersion
    item["installationCode"] = installationCode

    try:
        file = repo.get_contents("incidents/data.json", ref=branch)
    except:
        file = None
    if file is None:
        content = []
        content.append(item)
        repo.create_file(
            "incidents/data.json", "First incident", json.dumps(content), branch=branch
        )
        repo.create_file(
            f"incidents/{result}/data.json",
            f"Created {result} incident",
            json.dumps(item),
            branch=branch,
        )
    else:
        content = json.loads(file.decoded_content.decode())
        content.append(item)
        repo.update_file(
            "incidents/data.json",
            "acmsl-licdata",
            json.dumps(content),
            file.sha,
            branch=branch,
        )
        repo.create_file(
            f"incidents/{result}/data.json",
            f"Created {result} incident",
            json.dumps(item),
            branch=branch,
        )

    return result
