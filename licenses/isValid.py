import json
import os
import sys
from datetime import datetime

sys.path.insert(0, "deps")

from github import Github


def handler(event, context):

    token = os.environ["GITHUB_TOKEN"]

    headers = event.get("headers", {})
    host = headers.get("host", event.get("host", ""))
    response = {"headers": {"Content-Type": "application/json"}}

    status = 200
    file = None
    branch = "gh-pages"
    defaultComment = "acmsl-licdata-isValid-license"

    body = event.get("body", {})
    if body:
        body = json.loads(body)
        clientId = body.get("clientId", event.get("clientId", "missing"))
        installationCode = body.get(
            "installationCode", event.get("installationCode", "missing")
        )
    else:
        clientId = event.get("clientId", "missing")
        installationCode = event.get("installationCode", "missing")

    g = Github(token)
    repo = g.get_repo("acmsl/licdata")

    licenseId = findLicenseId(clientId, installationCode, repo, branch)

    if licenseId:
        try:
            file = repo.get_contents(f"licenses/{licenseId}/data.json", ref=branch)
        except:
            file = None
        if file:
            licenseContent = json.loads(file.decoded_content.decode())
            licenseEnd = datetime.fromisoformat(
                licenseContent.get("licenseEnd", "1970-01-01")
            )
            print("LicenseEnd: ")
            print(str(licenseEnd))
            if licenseEnd >= datetime.now():
                status = 200
            else:
                status = 410
    else:
        print("licenseId: not found")

    response["statusCode"] = status

    return response


def findPcId(licenseId, installationCode, repo, branch):
    try:
        allPcs = repo.get_contents("pcs.json", ref=branch)
    except:
        allPcs = None
    if allPcs:
        allPcsContent = json.loads(allPcs.decoded_content.decode())
        pcs = [x for x in allPcsContent if x["licenseId"] == licenseId]
        if pcs:
            for pc in pcs:
                pcId = pc["id"]
                try:
                    pcFile = repo.get_contents(f"pcs/{pcId}/data.json", ref=branch)
                except:
                    pcFile = None
                if pcFile:
                    pcContent = json.loads(pcFile.decoded_content.decode())
                    if pcContent["installationCode"] == installationCode:
                        return pcId
                else:
                    print(f"No pc file found at pcs/{pcId}/data.json")
        else:
            print(f"No pc found for license {licenseId}")

    return None


def findLicenseId(clientId, installationCode, repo, branch):
    try:
        allLicenses = repo.get_contents("licenses.json", ref=branch)
    except:
        allLicenses = None
    if allLicenses:
        allLicensesContent = json.loads(allLicenses.decoded_content.decode())
        licenses = [x for x in allLicensesContent if x["clientId"] == clientId]
        if licenses:
            for license in licenses:
                licenseId = license["id"]
                pcId = findPcId(licenseId, installationCode, repo, branch)
                if pcId:
                    return licenseId
        else:
            print(f"No license found for clientId {clientId}")

    return None
