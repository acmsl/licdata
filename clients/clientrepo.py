import json

import githubrepo


def findById(clientId):
    repo = githubrepo.getRepo()
    branch = githubrepo.getBranch()
    client = None
    try:
        file = repo.get_contents(f"clients/{clientId}/data.json", ref=branch)
    except:
        file = None
    if file:
        client = json.loads(file.decoded_content.decode())
    return client


def findByEmail(email):
    repo = githubrepo.getRepo()
    branch = githubrepo.getBranch()
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


def insert(email, address, contact, phone):
    repo = githubrepo.getRepo()
    branch = githubrepo.getBranch()
    result = githubrepo.newId()

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
        item["address"] = address
        item["contact"] = contact
        item["phone"] = phone
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
            item["address"] = address
            item["contact"] = contact
            item["phone"] = phone
            repo.create_file(
                f"clients/{result}/data.json",
                f"Created {result} client",
                json.dumps(item),
                branch=branch,
            )
    return result


def update(id, email, address, contact, phone):
    repo = githubrepo.getRepo()
    branch = githubrepo.getBranch()

    item = {}
    item["id"] = id
    item["email"] = email

    try:
        data = repo.get_contents("clients/data.json", ref=branch)
    except:
        data = None
    if data:
        content = json.loads(data.decoded_content.decode())
        existing = [x for x in content if x["id"] == id]
        if existing and existing[0]["email"] != email:
            remaining = [x for x in content if x["id"] != id]
            remaining.append(item)
            repo.update_file(
                "clients/data.json",
                f"Updated clients/data.json for client {id}",
                json.dumps(remaining),
                data.sha,
                branch=branch,
            )
    print(f"About to update clients/{id}/data.json")
    try:
        client = repo.get_contents(f"clients/{id}/data.json", ref=branch)
        print("client file found")
    except:
        client = None
    if client:
        item["email"] = email
        item["address"] = address
        item["contact"] = contact
        item["phone"] = phone
        print(json.dumps(item))
        repo.update_file(
            f"clients/{id}/data.json",
            f"Updated {id} client",
            json.dumps(item),
            client.sha,
            branch=branch,
        )
    else:
        print(f"clients/{id}/data.json not found")

    return item


def delete(id):
    repo = githubrepo.getRepo()
    branch = githubrepo.getBranch()

    try:
        data = repo.get_contents("clients/data.json", ref=branch)
    except:
        data = None
    if data:
        content = json.loads(data.decoded_content.decode())
        el = [x for x in content if x["id"] != id]
        repo.update_file(
            "clients/data.json",
            "Deleted client {id} from clients/data.json",
            json.dumps(el),
            data.sha,
            branch=branch,
        )
    try:
        client = repo.get_contents(f"clients/{id}/data.json", ref=branch)
    except:
        client = None
    if client:
        repo.delete_file(
            f"clients/{id}/data.json", f"Deleted {id} client", client.sha, branch=branch
        )
