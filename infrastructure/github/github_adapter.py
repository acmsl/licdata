from github_raw import get_contents, create_file, update_file, delete_file
from uuid import uuid4
import json
from datetime import datetime


def new_id():
    return str(uuid4())


def find_by_id(id, path):
    item = None

    data = None

    sha = None

    try:
        (data, sha) = get_contents(f"{path}/{id}/data.json")
    except:
        data = None

    if data:
        item = json.loads(data)

    return (item, sha)


def find_all_by_attributes(filter, path):
    result = []

    sha = None

    try:
        (all_items, sha) = get_contents(f"{path}/data.json")
    except:
        all_items = None
    if all_items:
        all_items_content = json.loads(all_items)
        item = {}
        for key in filter:
            item[key] = filter[key]
        result = [
            x for x in all_items_content if _attributes_match(x, item, filter.keys())
        ]

    return (result, sha)


def find_all_by_attribute(attribute_value, attribute_name, path):
    filter = {}
    filter[attribute_name] = attribute_value
    return find_all_by_attributes(filter, path)


def find_by_attribute(attribute_value, attribute_name, path):
    result = None

    (items, sha) = find_all_by_attribute(attribute_value, attribute_name, path)

    if items:
        result = items[0]
    else:
        print(f"No {path} with {attribute_name} {attribute_value}")

    return (result, sha)

def find_by_attributes(filter, path):
    result = None

    (items, sha) = find_all_by_attributes(filter, path)

    if items:
        result = items[0]
    else:
        print(f"No {path} found matching {filter}")

    return (result, sha)

def insert(entity, path, primary_key, filter_keys, attribute_names):
    result = new_id()
    created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = None
    sha = None
    item = {}
    item["id"] = result

    for attribute in primary_key + filter_keys:
        item[attribute] = entity.get(attribute)

    try:
        (data, sha) = get_contents(f"{path}/data.json")
    except:
        data = None
    if data is None:
        content = []
        content.append(item)
        create_file(
            f"{path}/data.json",
            json.dumps(content),
            f"First instance in {path} collection: {result}",
        )
    else:
        content = json.loads(data)
        entries = [x for x in content if _attributes_match(x, entity, filter_keys)]
        if entries:
            result = entries[0]["id"]
        else:
            content.append(item)
            update_file(
                f"{path}/data.json",
                json.dumps(content),
                f"Updated {result} in {path} collection",
                sha,
            )

    for attribute in [ x for x in attribute_names if entity.get(attribute) is not None ]:
        item[attribute] = entity.get(attribute)
    item["id"] = result
    item["_created"] = created
    print(f"Inserting {item} in {path}/{result}/data.json")
    create_file(
        f"{path}/{result}/data.json",
        json.dumps(item),
        f"Created a new entry {result} in {path} collection",
    )

    return result


def _attributes_match(item, target, attribute_names):
    result = True

    for attribute_name in attribute_names:
        if item.get(attribute_name) != target.get(attribute_name):
            result = False
            break

    return result


def update(entity, path, primary_key, filter_keys, attribute_names):

    id = entity.get("id")
    item = {}
    item["id"] = id
    for attribute in primary_key + filter_keys:
        item[attribute] = entity.get(attribute)
    try:
        (data, sha) = get_contents(f"{path}/data.json")
    except:
        data = None
    if data:
        content = json.loads(data)
        existing = [x for x in content if x.get("id") == id]
        if existing and not _attributes_match(existing[0], entity, attribute_names):
            remaining = [x for x in content if x.get("id") != id]
            remaining.append(item)
            update_file(
                f"{path}/data.json",
                json.dumps(remaining),
                f"Updated {id} in {path}/data.json",
                sha,
            )
    try:
        (old_item, oldSha) = get_contents(f"{path}/{id}/data.json")
    except:
        old_item = None
    if old_item:
        for attribute in attribute_names:
            item[attribute] = entity.get(attribute)
        item["id"] = id
        item["_created"] = entity.get("_created")
        item["_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        update_file(
            f"{path}/{id}/data.json",
            json.dumps(item),
            f"Updated {path}/{id}/data.json",
            oldSha,
        )
    else:
        print(f"{path}/{id}/data.json not found")

    return item


def delete(id, path):
    result = False

    try:
        (data, sha) = get_contents(f"{path}/data.json")
    except:
        data = None
    if data:
        content = json.loads(data)
        existing = [x for x in content if x.get("id") != id]
        update_file(
            f"{path}/data.json",
            json.dumps(existing),
            f"Deleted {id} from {path}/data.json",
            sha,
        )

        delete_file(
            f"{path}/{id}/data.json", f"Deleted {path}/{id}/data.json"
        )
        result = True

    return result


def list(path):
    result = []
    sha = None

    try:
        (data, sha) = get_contents(f"{path}/data.json")
        print(f"{path}/data.json -> {data}")
    except:
        data = None
    if data:
        result = json.loads(data)

    return (result, sha)
