import json


def findClientByEmail(email, repo, branch):
    try:
        allClients = repo.get_contents("clients.json", ref=branch)
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
