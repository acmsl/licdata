import json

import pcrepo
import clientrepo


def findLicenseIdByClientIdAndInstallationCode(
    clientId, installationCode, repo, branch
):
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


def findLicenseIdByEmailProductAndInstallationCode(
    email, product, productVersion, installationCode, repo, branch
):
    client = clientrepo.findClientByEmail(email, repo, branch)
    if client:
        clientId = client.get("id", "missing")
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
                    pcId = pcrepo.findPcIdByLicenseIdProductAndInstallationCode(
                        licenseId,
                        product,
                        productVersion,
                        installationCode,
                        repo,
                        branch,
                    )
                    if pcId:
                        return licenseId
            else:
                print(f"No license found for clientId {clientId}")
    else:
        print(f"No client found for email {email}")

    return None
