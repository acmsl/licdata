import json
from github import Github
import os
import sys

sys.path.insert(0, "common")

import clientrepo
import licenserepo
import params
import pcrepo


def handler(event, context):

    token = os.environ["GITHUB_TOKEN"]
    repository = os.environ["GITHUB_REPO"]
    branch = os.environ["GITHUB_BRANCH"]

    headers = event.get("headers", {})
    host = headers.get("host", event.get("host", ""))
    response = {
        "headers": {"Content-Type": "application/json"},
        "event": str(event),
        "context": str(context),
    }

    status = 200
    file = None

    body = event.get("body", {})
    if body:
        body = json.loads(body)

    g = Github(token)
    repo = g.get_repo("acmsl/licdata")

    email = params.retrieveEmail(body, event)

    client = clientrepo.findByEmail(email, repo, branch)
    if client:
        clientId = client["id"]
    else:
        clientId = clientrepo.insert(email, repo, branch)

    productName = params.retrieveProduct(body, event)
    productVersion = params.retrieveProductVersion(body, event)
    installationCode = params.retrieveInstallationCode(body, event)
    description = params.retrieveDescription(body, event)

    pc = pcrepo.findByProductAndInstallationCode(
        productName, productVersion, installationCode, repo, branch
    )
    if not pc:
        pcId = pcrepo.insert(
            productName,
            productVersion,
            installationCode,
            description,
            repo,
            branch,
        )

    client = clientrepo.findByEmail(email, repo, branch)
    if client:
        clientId = client["id"]
    else:
        clientId = clientrepo.insert(email, repo, branch)

    license = licenserepo.findByClientIdProductAndInstallationCode(
        clientId, productName, productVersion, installationCode, repo, branch
    )
    if not license:
        licenseId = licenserepo.insert(
            clientId,
            repo,
            branch,
        )
        if license:
            status = 201

    if licenseId:
        response["headers"].update({"Location": f"https://{host}/license/{licenseId}"})

    response["statusCode"] = status

    return response
