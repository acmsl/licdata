import json
import os
import sys
import datetime

sys.path.insert(0, "common")

from github import Github

import licenserepo
import params


def handler(event, context):

    token = os.environ["GITHUB_TOKEN"]
    repository = os.environ["GITHUB_REPO"]
    branch = os.environ["GITHUB_BRANCH"]

    headers = event.get("headers", {})
    host = headers.get("host", event.get("host", ""))
    response = {"headers": {"Content-Type": "application/json"}}

    status = 410
    file = None

    body = event.get("body", {})
    if body:
        body = json.loads(body)

    g = Github(token)
    repo = g.get_repo(repository)

    print(body)

    licenseId = licenserepo.findLicenseIdByEmailProductAndInstallationCode(
        params.retrieveEmail(body, event),
        params.retrieveProduct(body, event),
        params.retrieveProductVersion(body, event),
        params.retrieveInstallationCode(body, event),
        repo,
        branch,
    )

    if licenseId:
        license = licenserepo.findById(licenseId, repo, branch)
        if license:
            if license["licenseEnd"] >= datetime.datetime.now():
                status = 200
            else:
                status = 410
        else:
            status = 404
    else:
        print("licenseId: not found")
        status = 404

    response["statusCode"] = status

    return response
