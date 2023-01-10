from uuid import uuid4
import os
from github import Github
import json


def getRepo():
    token = os.environ["GITHUB_TOKEN"]
    github = Github(token)
    repository = os.environ["GITHUB_REPO"]
    return github.get_repo(repository)


def getBranch():
    return os.environ["GITHUB_BRANCH"]


def newId():
    return str(uuid4())


def findById(id, entityType):
    repo = getRepo()
    branch = getBranch()
    item = None
    try:
        file = repo.get_contents(f"{entityType}/{id}/data.json", ref=branch)
    except:
        file = None
    if file:
        item = json.loads(file.decoded_content.decode())
    return item


def findByAttribute(attributeValue, attributeName, entityType):
    repo = githubrepo.getRepo()
    branch = githubrepo.getBranch()
    result = None

    try:
        allItems = repo.get_contents(f"{entityType}/data.json", ref=branch)
    except:
        allItems = None
    if allClients:
        allItemsContent = json.loads(allItems.decoded_content.decode())
        items = [x for x in allItemsContent if x.get(attributeName) == attributeValue]
        if items:
            result = items[0]
        else:
            print(f"No {entityType} with {attributeName} {attributeValue}")

    return result


def insert(entity, entityType, filterKeys, attributeNames):
    repo = githubrepo.getRepo()
    branch = githubrepo.getBranch()
    result = None
    item = {}
    for attribute in filterKeys:
        item[attribute] = entity.get(attribute)

    try:
        file = repo.get_contents(f"{entityType}/data.json", ref=branch)
    except:
        file = None
    if file is None:
        result = githubrepo.newId()
        item["id"] = result
        content = []
        content.append(item)
        repo.create_file(
            f"{entityType}/data.json",
            f"First instance in {entityType} collection",
            json.dumps(content),
            branch=branch,
        )
        nonFilterKeyAttributes = [
            attr for attr in attributeNames if attr not in filterKeys
        ]
        for attribute in nonFilterKeyAttributes:
            item[attribute] = entity.get(attribute)
        repo.create_file(
            f"{entityType}/{result}/data.json",
            f"Created a new {entityType} entry with id {result}",
            json.dumps(item),
            branch=branch,
        )
    else:
        content = json.loads(file.decoded_content.decode())
        entries = [x for x in content if _attributesMatch(x, entity, filterKeys)]
        if entries:
            result = entries[0]["id"]
        else:
            result = githubrepo.newId()
            item["id"] = result
            content.append(item)
            repo.update_file(
                f"{entityType}/data.json",
                f"Updated {result} in {entityType} collection",
                json.dumps(content),
                file.sha,
                branch=branch,
            )
            for attribute in attributeNames:
                item[attribute] = entity.get(attribute)
            repo.create_file(
                f"{entityType}/{result}/data.json",
                f"Created a new entry {result} in {entityType} collection",
                json.dumps(item),
                branch=branch,
            )
    return result


def _attributesMatch(item, target, attributeNames):
    result = True

    for attributeName in attributeNames:
        if item.get(attributeName) != target.get(attributeName):
            result = False
            break

    return result


def update(entity, entityType, filterKeys, attributeNames):
    repo = githubrepo.getRepo()
    branch = githubrepo.getBranch()

    id = entity.get("id")
    item = {}
    for attribute in filterKeys:
        item[attribute] = entity.get(attribute)

    try:
        data = repo.get_contents(f"{entityType}/data.json", ref=branch)
    except:
        data = None
    if data:
        content = json.loads(data.decoded_content.decode())
        existing = [x for x in content if x.get("id") == id]
        if existing and not _attributesMatch(existing[0], entity, attributeNames):
            remaining = [x for x in content if x.get("id") != id]
            remaining.append(item)
            repo.update_file(
                f"{entityType}/data.json",
                f"Updated {id} in {entityType}/data.json",
                json.dumps(remaining),
                data.sha,
                branch=branch,
            )
    try:
        oldItem = repo.get_contents(f"{entityType}/{id}/data.json", ref=branch)
    except:
        oldItem = None
    if oldItem:
        nonFilterKeyAttributes = [
            attr for attr in attributeNames if attr not in filterKeys
        ]
        for attribute in nonFilterKeyAttributes:
            item[attribute] = entity.get(attribute)
        repo.update_file(
            f"{entityType}/{id}/data.json",
            f"Updated {entityType}/{id}/data.json",
            json.dumps(item),
            oldItem.sha,
            branch=branch,
        )
    else:
        print(f"{entityType}/{id}/data.json not found")

    return item


def delete(id, entityType):
    repo = githubrepo.getRepo()
    branch = githubrepo.getBranch()
    result = False

    try:
        data = repo.get_contents(f"{entityType}/data.json", ref=branch)
    except:
        data = None
    if data:
        content = json.loads(data.decoded_content.decode())
        existing = [x for x in content if x.get("id") != id]
        repo.update_file(
            f"{entityType}/data.json",
            "Deleted {id} from {entityType}/data.json",
            json.dumps(existing),
            data.sha,
            branch=branch,
        )
    try:
        item = repo.get_contents(f"{entityType}/{id}/data.json", ref=branch)
    except:
        item = None
    if item:
        repo.delete_file(
            f"{entityType}/{id}/data.json",
            f"Deleted {entityType}/{id}",
            client.sha,
            branch=branch,
        )
        result = True

    return result
