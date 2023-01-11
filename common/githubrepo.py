from uuid import uuid4
import os
from github import Github
import json
import githubraw


def newId():
    return str(uuid4())


def findById(id, entityType):
    item = None
    try:
        file = githubraw.getContents(f"{entityType}/{id}/data.json")
    except:
        file = None

    if file:
        item = json.loads(file.decoded_content.decode())

    return item


def findAllByAttributes(filter, entityType):
    result = []

    try:
        allItems = githubraw.getContents(f"{entityType}/data.json")
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
    result = None
    item = {}

    for attribute in filterKeys:
        item[attribute] = entity.get(attribute)

    try:
        file = githubraw.getContents(f"{entityType}/data.json")
    except:
        file = None
    if file is None:
        result = newId()
        item["id"] = result
        content = []
        content.append(item)
        githubraw.createFile(
            f"{entityType}/data.json",
            json.dumps(content),
            f"First instance in {entityType} collection",
        )
        nonFilterKeyAttributes = [
            attr for attr in attributeNames if attr not in filterKeys
        ]
        for attribute in nonFilterKeyAttributes:
            item[attribute] = entity.get(attribute)
        githubraw.createFile(
            f"{entityType}/{result}/data.json",
            json.dumps(item),
            f"Created a new {entityType} entry with id {result}",
        )
    else:
        content = json.loads(file.decoded_content.decode())
        entries = [x for x in content if _attributesMatch(x, entity, filterKeys)]
        if entries:
            result = entries[0]["id"]
        else:
            result = newId()
            item["id"] = result
            content.append(item)
            githubraw.updateFile(
                f"{entityType}/data.json",
                json.dumps(content),
                f"Updated {result} in {entityType} collection",
                file.sha,
            )
            for attribute in attributeNames:
                item[attribute] = entity.get(attribute)
            githubraw.createFile(
                f"{entityType}/{result}/data.json",
                json.dumps(item),
                f"Created a new entry {result} in {entityType} collection",
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
        data = githubraw.getContents(f"{entityType}/data.json")
    except:
        data = None
    if data:
        content = json.loads(data.decoded_content.decode())
        existing = [x for x in content if x.get("id") == id]
        if existing and not _attributesMatch(existing[0], entity, attributeNames):
            remaining = [x for x in content if x.get("id") != id]
            remaining.append(item)
            githubraw.updateFile(
                f"{entityType}/data.json",
                json.dumps(remaining),
                f"Updated {id} in {entityType}/data.json",
                data.sha,
            )
    try:
        oldItem = githubraw.getContents(f"{entityType}/{id}/data.json")
    except:
        oldItem = None
    if oldItem:
        nonFilterKeyAttributes = [
            attr for attr in attributeNames if attr not in filterKeys
        ]
        for attribute in nonFilterKeyAttributes:
            item[attribute] = entity.get(attribute)
        githubraw.updateFile(
            f"{entityType}/{id}/data.json",
            json.dumps(item),
            f"Updated {entityType}/{id}/data.json",
            oldItem.sha,
        )
    else:
        print(f"{entityType}/{id}/data.json not found")

    return item


def delete(id, entityType):
    (repo, branch, key) = getRepoBranchAndKey()
    result = False

    try:
        data = githubraw.getContents(f"{entityType}/data.json")
    except:
        data = None
    if data:
        content = json.loads(data.decoded_content.decode())
        existing = [x for x in content if x.get("id") != id]
        githubraw.updateFile(
            f"{entityType}/data.json",
            json.dumps(existing),
            "Deleted {id} from {entityType}/data.json",
            data.sha,
        )
    try:
        item = githubraw.getContents(f"{entityType}/{id}/data.json")
    except:
        item = None
    if item:
        githubraw.deleteFile(
            f"{entityType}/{id}/data.json",
            f"Deleted {entityType}/{id}/data.json",
            item.sha,
        )
        result = True

    return result


def list(entityType):
    (repo, branch, key) = getRepoBranchAndKey()
    result = []

    try:
        data = githubraw.getContents(f"{entityType}/data.json")
    except:
        data = None
    if data:
        result = json.loads(data.decoded_content.decode())

    return result
