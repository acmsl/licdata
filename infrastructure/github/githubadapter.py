from uuid import uuid4
import json
import githubraw


def newId():
    return str(uuid4())


def findById(id, entityType):
    item = None

    data = None

    sha = None

    try:
        (data, sha) = githubraw.getContents(f"{entityType}/{id}/data.json")
    except:
        data = None

    if data:
        item = json.loads(data)

    return (item, sha)


def findAllByAttributes(filter, entityType):
    result = []

    sha = None

    print(filter)

    try:
        (allItems, sha) = githubraw.getContents(f"{entityType}/data.json")
    except:
        allItems = None
    if allItems:
        allItemsContent = json.loads(allItems)
        item = {}
        for key in filter:
            item[key] = filter[key]
        result = [
            x for x in allItemsContent if _attributesMatch(x, item, filter.keys())
        ]

    return (result, sha)


def findAllByAttribute(attributeValue, attributeName, entityType):
    filter = {}
    filter[attributeName] = attributeValue
    return findAllByAttributes(filter, entityType)


def findByAttribute(attributeValue, attributeName, entityType):
    result = None

    (items, sha) = findAllByAttribute(attributeValue, attributeName, entityType)

    if items:
        result = items[0]
    else:
        print(f"No {entityType} with {attributeName} {attributeValue}")

    return (result, sha)

def findByAttributes(filter, entityType):
    result = None

    (items, sha) = findAllByAttributes(filter, entityType)

    if items:
        result = items[0]
    else:
        print(f"No {entityType} found matching {filter}")

    return (result, sha)

def insert(entity, entityType, filterKeys, attributeNames):
    result = None
    item = {}
    data = None
    sha = None

    for attribute in filterKeys:
        item[attribute] = entity.get(attribute)

    try:
        (data, sha) = githubraw.getContents(f"{entityType}/data.json")
    except:
        data = None
    if data is None:
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
        content = json.loads(data)
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
                sha,
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

    id = entity.get("id")
    item = {}
    item["id"] = id
    print(entity)
    for attribute in filterKeys:
        item[attribute] = entity.get(attribute)
    print(item)
    try:
        (data, sha) = githubraw.getContents(f"{entityType}/data.json")
    except:
        data = None
    if data:
        content = json.loads(data)
        existing = [x for x in content if x.get("id") == id]
        if existing and not _attributesMatch(existing[0], entity, attributeNames):
            remaining = [x for x in content if x.get("id") != id]
            remaining.append(item)
            githubraw.updateFile(
                f"{entityType}/data.json",
                json.dumps(remaining),
                f"Updated {id} in {entityType}/data.json",
                sha,
            )
    try:
        (oldItem, oldSha) = githubraw.getContents(f"{entityType}/{id}/data.json")
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
            oldSha,
        )
    else:
        print(f"{entityType}/{id}/data.json not found")

    return item


def delete(id, entityType):
    result = False

    try:
        (data, sha) = githubraw.getContents(f"{entityType}/data.json")
    except:
        data = None
    if data:
        content = json.loads(data)
        existing = [x for x in content if x.get("id") != id]
        githubraw.updateFile(
            f"{entityType}/data.json",
            json.dumps(existing),
            f"Deleted {id} from {entityType}/data.json",
            sha,
        )

        githubraw.deleteFile(
            f"{entityType}/{id}/data.json", f"Deleted {entityType}/{id}/data.json"
        )
        result = True

    return result


def list(entityType):
    result = []
    sha = None

    try:
        (data, sha) = githubraw.getContents(f"{entityType}/data.json")
        print(f"{entityType}/data.json -> {data}")
    except:
        data = None
    if data:
        result = json.loads(data)

    return (result, sha)
