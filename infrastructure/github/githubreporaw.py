from uuid import uuid4
import json
import githubraw


def newId():
    return str(uuid4())


def findById(id, entityType):
    item = None
    try:
        file = githubraw.getContents(f"{entityType}/{id}/data.json", repo, branch, key)

    except:
        file = None

    if file:
        item = json.loads(file.decoded_content.decode())

    return item


def findAllByAttributes(filter, entityType):
    result = []

    try:
        allItems = (
            githubraw.getContents(f"{entityType}/data.json", repo, branch, key),
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
    result = None
    item = {}

    for attribute in filterKeys:
        item[attribute] = entity.get(attribute)

    try:
        file = githubraw.getContents(f"{entityType}/data.json", repo, branch, key)
    except:
        file = None
    if file is None:
        result = newId()
        item["id"] = result
        print(item)
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

    id = entity.get("id")
    item = {}
    item["id"] = id
    print(entity)
    for attribute in filterKeys:
        item[attribute] = entity.get(attribute)
    print(item)
    try:
        data = githubraw.getContents(f"{entityType}/data.json", repo, branch, key)
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
        oldItem = githubraw.getContents(
            f"{entityType}/{id}/data.json", repo, branch, key
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
    result = False

    try:
        data = githubraw.getContents(f"{entityType}/data.json", repo, branch, key)
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
        item = githubraw.getContents(f"{entityType}/{id}/data.json", repo, branch, key)
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
    result = []

    try:
        data = githubraw.getContents(f"{entityType}/data.json", repo, branch, key)
    except:
        data = None
    if data:
        result = json.loads(data.decoded_content.decode())

    return result
