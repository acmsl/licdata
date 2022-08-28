import json
import os
import sys

sys.path.insert(0, "deps")

from github import Github
from uuid import uuid4


def handler(event, context):

    token = os.environ["GITHUB_TOKEN"]

    headers = event.get("headers", {})
    host = headers.get("host", event.get("host", ""))
    response = {
        "headers": {"Content-Type": "application/json"},
        "event": str(event),
        "context": str(context),
    }

    status = 200
    file = None
    branch = "gh-pages"
    defaultComment = "acmsl-licdata-post-client"

    body = event.get("body", {})
    if body:
        body = json.loads(body)
        bundle = body.get("bundle", event.get("bundle", "missing"))
        email = body.get("email", event.get("email", "missing"))
    else:
        bundle = event.get("bundle", "missing")
        email = event.get("email", "missing")

    g = Github(token)
    repo = g.get_repo("acmsl/licdata")

    try:
        file = repo.get_contents("clients.json", ref=branch)
    except:
        file = None
    if file is None:
        content = []
        clientId = str(uuid4())
        item = {}
        item["clientId"] = clientId
        item["email"] = email
        content.append(item)
        repo.create_file(
            "clients.json", "First client", json.dumps(content), branch=branch
        )
        status = 201

    else:
        content = json.loads(file.decoded_content.decode())
        el = [x for x in content if x["email"] == email]
        if el:
            clientId = el[0]["clientId"]
        else:
            clientId = str(uuid4())
            item = {}
            item["clientId"] = clientId
            item["email"] = email
            content.append(item)
            status = 201
        repo.update_file(
            "clients.json",
            defaultComment,
            json.dumps(content),
            file.sha,
            branch=branch,
        )

    content = {}
    content["id"] = clientId
    content["bundle"] = bundle
    content["email"] = email

    try:
        file = repo.get_contents(f"clients/{clientId}/data.json", ref=branch)
    except:
        file = None
    if file is None:
        repo.create_file(
            f"clients/{clientId}/data.json",
            defaultComment,
            json.dumps(content),
            branch=branch,
        )
        status = 201
    else:
        repo.update_file(
            f"clients/{clientId}/data.json",
            defaultComment,
            json.dumps(content),
            file.sha,
            branch=branch,
        )

    response["headers"].update({"Location": f"https://{host}/clients/{clientId}"})

    response["statusCode"] = status

    return response
