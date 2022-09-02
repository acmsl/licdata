import json
from uuid import uuid4
import os
from github import Github


def findById(clientId):
    token = os.environ["GITHUB_TOKEN"]
    github = Github(token)
    repository = os.environ["GITHUB_REPO"]
    repo = github.get_repo(repository)
    branch = os.environ["GITHUB_BRANCH"]
    client = None
    try:
        file = repo.get_contents(f"clients/{clientId}/data.json", ref=branch)
    except:
        file = None
    if file:
        client = json.loads(file.decoded_content.decode())
    return client


def insert(email):
    token = os.environ["GITHUB_TOKEN"]
    github = Github(token)
    repository = os.environ["GITHUB_REPO"]
    repo = github.get_repo(repository)
    branch = os.environ["GITHUB_BRANCH"]
    result = str(uuid4())

    item = {}
    item["id"] = result
    item["email"] = email

    try:
        file = repo.get_contents("clients/data.json", ref=branch)
    except:
        file = None
    if file is None:
        content = []
        content.append(item)
        repo.create_file(
            "clients/data.json", "First client", json.dumps(content), branch=branch
        )
        repo.create_file(
            f"clients/{result}/data.json",
            f"Created {result} client",
            json.dumps(item),
            branch=branch,
        )
    else:
        content = json.loads(file.decoded_content.decode())
        el = [x for x in content if x["email"] == email]
        if el:
            result = el[0]["id"]
        else:
            content.append(item)
            repo.update_file(
                "clients/data.json",
                "acmsl-licdata",
                json.dumps(content),
                file.sha,
                branch=branch,
            )
            repo.create_file(
                f"clients/{result}/data.json",
                f"Created {result} client",
                json.dumps(item),
                branch=branch,
            )
    return result


def findByEmail(email):
    token = os.environ["GITHUB_TOKEN"]
    github = Github(token)
    repository = os.environ["GITHUB_REPO"]
    repo = github.get_repo(repository)
    branch = os.environ["GITHUB_BRANCH"]
    try:
        allClients = repo.get_contents("clients/data.json", ref=branch)
    except:
        allClients = None
    if allClients:
        allClientsContent = json.loads(allClients.decoded_content.decode())
        clients = [x for x in allClientsContent if x["email"] == email]
        if clients:
            return clients[0]
        else:
            print(f"No client found for email {email}")

    return None
