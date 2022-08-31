import json
from uuid import uuid4


def insert(email, repo, branch):
    result = str(uuid4())

    try:
        file = repo.get_contents("clients.json", ref=branch)
    except:
        file = None
    if file is None:
        content = []
        item = {}
        item["id"] = result
        item["email"] = email
        content.append(item)
        repo.create_file(
            "clients.json", "First client", json.dumps(content), branch=branch
        )
    else:
        content = json.loads(file.decoded_content.decode())
        el = [x for x in content if x["email"] == email]
        if el:
            result = el[0]["id"]
        else:
            item = {}
            item["id"] = result
            item["email"] = email
            content.append(item)
            repo.update_file(
                "clients.json",
                "acmsl-licdata",
                json.dumps(content),
                file.sha,
                branch=branch,
            )

    return result


def findByEmail(email, repo, branch):
    try:
        allClients = repo.get_contents("clients.json", ref=branch)
    except:
        allClients = None
    if allClients:
        allClientsContent = json.loads(allClients.decoded_content.decode())
        clients = [x for x in allClientsContent if x["email"] == email]
        if clients:
            print(f"Clients associated to {email}: {clients}")
            return clients[0]
        else:
            print(f"No client found for email {email}")

    return None
