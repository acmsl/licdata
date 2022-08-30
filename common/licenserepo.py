import json

from pcrepo import findPcId


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
