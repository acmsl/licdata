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


def getKey():
    return os.environ["KEY"]


def getRepoBranchAndKey():
    return (getRepo(), getBranch(), getKey())


def newId():
    return str(uuid4())


def encrypt(content, key):
    result = None
    fernet = Fernet(key)

    try:
        result = fernet.encrypt(content.encode())
    except:
        print(f"{content} could not be encrypted")

    return result


def decrypt(content, key):
    result = None
    fernet = Fernet(key)

    try:
        result = fernet.decrypt(content).decode()
    except:
        print(f"{content} could not be decrypted")

    return result


def decryptFile(file, filePath, key):
    result = None
    fernet = Fernet(key)

    decFile = decrypt(file.decoded_content.decode(), key)

    if decFile:
        result = json.loads(decFile.decode())
    else:
        print(f"{filePath} could not be decrypted")

    return result


def findById(id, entityType):
    (repo, branch, key) = getRepoBranchAndKey()
    item = None
    try:
        file = decryptFile(
            repo.get_contents(f"{entityType}/{id}/data.json", ref=branch),
            f"{entityType}/{id}/data.json",
            key,
        )
    except:
        file = None

    if file:
        item = json.loads(file.decoded_content.decode())

    return item


def findAllByAttributes(filter, entityType):
    (repo, branch, key) = getRepoBranchAndKey()
    result = []

    try:
        allItems = decryptFile(
            repo.get_contents(f"{entityType}/data.json", ref=branch),
            f"{entityType}/data.json",
            key,
        )
    except:
        allItems = None
    if allItems:
        allItemsContent = json.loads(allItems.decoded_content.decode())
        item = {}
        for key in filter:
            item[key] = filter.get(key)
        result = [
            x for x in allItemsContent if _attributesMatch(x, item, filter.keys())
        ]

    return result


def findAllByAttribute(attributeValue, attributeName, entityType):
    filter = {}
    filter[attributeName] = attributeValue
    return findAllByAttributes(filter, entityType)


def findByAttribute(attributeValue, attributeName, entityType):
    items = findAllByAttribute(attributeValue, attributeName, entityType)
    result = None

    if items:
        result = items[0]
    else:
        print(f"No {entityType} with {attributeName} {attributeValue}")

    return result


def insert(entity, entityType, filterKeys, attributeNames):
    (repo, branch, key) = getRepoBranchAndKey()
    result = None
    item = {}

    for attribute in filterKeys:
        item[attribute] = entity.get(attribute)

    try:
        file = decryptFile(
            repo.get_contents(f"{entityType}/data.json", ref=branch),
            f"{entityType}/data.json",
            key,
        )
    except:
        file = None
    if file is None:
        result = newId()
        item["id"] = result
        print("In githubrepo#92")
        print(item)
        content = []
        content.append(item)
        repo.create_file(
            f"{entityType}/data.json",
            f"First instance in {entityType} collection",
            encrypt(json.dumps(content), key),
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
            encrypt(json.dumps(item), key),
            branch=branch,
        )
    else:
        content = json.loads(file.decoded_content.decode())
        entries = [x for x in content if _attributesMatch(x, entity, filterKeys)]
        if entries:
            result = entries[0]["id"]
        else:
            result = newId()
            item["id"] = result
            print("In githubrepo#121")
            print(item)
            content.append(item)
            repo.update_file(
                f"{entityType}/data.json",
                f"Updated {result} in {entityType} collection",
                encrypt(json.dumps(content), key),
                file.sha,
                branch=branch,
            )
            for attribute in attributeNames:
                item[attribute] = entity.get(attribute)
            repo.create_file(
                f"{entityType}/{result}/data.json",
                f"Created a new entry {result} in {entityType} collection",
                encrypt(json.dumps(item), key),
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
    (repo, branch, key) = getRepoBranchAndKey()

    id = entity.get("id")
    item = {}
    item["id"] = id
    print(entity)
    for attribute in filterKeys:
        item[attribute] = entity.get(attribute)
    print(item)
    try:
        data = decryptFile(
            repo.get_contents(f"{entityType}/data.json", ref=branch),
            f"{entityType}/data.json",
            key,
        )
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
                encrypt(json.dumps(remaining), key),
                data.sha,
                branch=branch,
            )
    try:
        oldItem = decryptFile(
            repo.get_contents(f"{entityType}/{id}/data.json", ref=branch),
            f"{entityType}/{id}/data.json",
            key,
        )
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
            encrypt(json.dumps(item), key),
            oldItem.sha,
            branch=branch,
        )
    else:
        print(f"{entityType}/{id}/data.json not found")

    return item


def delete(id, entityType):
    (repo, branch, key) = getRepoBranchAndKey()
    result = False

    try:
        data = decryptFile(
            repo.get_contents(f"{entityType}/data.json", ref=branch),
            f"{entityType}/data.json",
            key,
        )
    except:
        data = None
    if data:
        content = json.loads(data.decoded_content.decode())
        existing = [x for x in content if x.get("id") != id]
        repo.update_file(
            f"{entityType}/data.json",
            "Deleted {id} from {entityType}/data.json",
            encrypt(json.dumps(existing), key),
            data.sha,
            branch=branch,
        )
    try:
        item = decryptFile(
            repo.get_contents(f"{entityType}/{id}/data.json", ref=branch),
            f"{entityType}/{id}/data.json",
            key,
        )
    except:
        item = None
    if item:
        repo.delete_file(
            f"{entityType}/{id}/data.json",
            f"Deleted {entityType}/{id}/data.json",
            item.sha,
            branch=branch,
        )
        result = True

    return result


def list(entityType):
    (repo, branch, key) = getRepoBranchAndKey()
    result = []

    try:
        data = decryptFile(
            repo.get_contents(f"{entityType}/data.json", ref=branch),
            f"{entityType}/data.json",
            key,
        )
    except:
        data = None
    if data:
        result = json.loads(data.decoded_content.decode())

    return result
