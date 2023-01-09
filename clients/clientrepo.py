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
