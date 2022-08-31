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
    productName = params.retrieveProduct(body, event)
    productVersion = params.retrieveProductVersion(body, event)
    installationCode = params.retrieveInstallationCode(body, event)
    description = params.retrieveDescription(body, event)

    client = clientrepo.findByEmail(email, repo, branch)
    if client:
        clientId = client["id"]
    else:
        clientId = clientrepo.insert(email, repo, branch)
        print(f"Inserting new client {email} -> {clientId}")

    license = licenserepo.findByClientIdAndInstallationCode(
        clientId, installationCode, repo, branch
    )
    if license:
        licenseId = license["id"]
    else:
        licenseId = licenserepo.insert(
            clientId,
            productName,
            productVersion,
            repo,
            branch,
        )
        print(f"Inserting new license for client {clientId} -> {licenseId}")
        if license:
            status = 201

    pc = pcrepo.findByInstallationCode(installationCode, repo, branch)
    if pc:
        if not licenseId in pc["licenses"]:
            pcId = pc["id"]
            print(f"Adding license {licenseId} to {pcId}")
            pcrepo.addLicense(pc["id"], licenseId, repo, branch)
        else:
            pcId = pcrepo.insert(
                [licenseId],
                installationCode,
                description,
                repo,
                branch,
            )
            print(f"Inserting new pc for license {licenseId} -> {pcId}")
    else:
        pcId = pcrepo.insert(
            [licenseId],
            installationCode,
            description,
            repo,
            branch,
        )
        print(f"Inserting new pc for license {licenseId} -> {pcId}")

    if licenseId:
        response["headers"].update({"Location": f"https://{host}/license/{licenseId}"})

    response["statusCode"] = status

    return response
