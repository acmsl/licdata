import json
import os
import sys

sys.path.insert(0, "deps")

from github import Github
from base64 import b64encode, b64decode


def handler(event, context):

    token = os.environ["GITHUB_TOKEN"]

    status = 200

    body = json.loads(str(event["body"]))
    data = body["data"]
    userId = body["userId"]

    b64userId = str(b64encode(bytes(userId, "utf-8")), "utf-8")
    userIdPath = userId
    productId = body["productId"]
    b64productId = str(b64encode(bytes(productId, "utf-8")), "utf-8")
    productIdPath = productId

    g = Github(token)
    repo = g.get_repo("acmsl/licdata")

    content = {}
    content["id"] = productId
    content["userId"] = userId
    content.update(data)
    file = None
    branch = "gh-pages"
    defaultComment = "acmsl-licdata-post-product"

    try:
        file = repo.get_contents(
            f"docs/{userIdPath}/products/{productIdPath}/data.json", ref=branch
        )
    except:
        file = None
    if file is None:
        repo.create_file(
            f"docs/{userIdPath}/products/{productIdPath}/data.json",
            defaultComment,
            json.dumps(content),
            branch=branch,
        )
        status = 201
    else:
        repo.update_file(
            f"docs/{userIdPath}/products/{productIdPath}/data.json",
            defaultComment,
            json.dumps(content),
            file.sha,
            branch=branch,
        )

    item = {}
    item["userId"] = userId
    try:
        file = repo.get_contents(f"docs/users.json", ref=branch)
    except:
        file = None
    if file is None:
        content = []
        conntent.append(item)
        repo.create_file(
            f"docs/users.json", "First user", json.dumps(content), branch=branch
        )
    else:
        content = json.loads(file.decoded_content.decode())
        print(len(content))
        el = [x for x in content if x["userId"] == userId]
        if el:
            content = list(filter(lambda x: x["userId"] != userId, content))
            content.append(item)
        else:
            content.append(item)
        repo.update_file(
            f"docs/users.json",
            "First user",
            json.dumps(content),
            file.sha,
            branch=branch,
        )

    response = {"statusCode": status, "body": str(content)}

    return response


"""

    response = {"statusCode": status}

    return response
"""
