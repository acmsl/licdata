import json

import pcrepo
import clientrepo

from datetime import datetime
from uuid import uuid4


def insert(clientId, repo, branch):
    result = str(uuid4())

    now = datetime.now()
    orderDate = now.strftime("%Y/%m/%d")
    deliveryDate = orderDate
    licenseType = ""
    licenseEnd = (now + datetime.timedelta(days=2)).strftime("%Y/%m/%d")
    item = {}
    item["id"] = result
    item["clientId"] = clientId
    item["orderDate"] = orderDate
    item["deliveryDate"] = deliveryDate
    item["licenseType"] = licenseType
    item["licenseEnd"] = licenseEnd

    try:
        file = repo.get_contents("licenses.json", ref=branch)
    except:
        file = None
    if file is None:
        now = datetime.now()
        content = []
        content.append(item)
        repo.create_file(
            "licenses.json", "First license", json.dumps(content), branch=branch
        )
    else:
        content = json.loads(file.decoded_content.decode())
        content.append(item)
        repo.update_file(
            "licenses.json",
            "acmsl-licdata",
            json.dumps(content),
            file.sha,
            branch=branch,
        )

    return result


def findByClientIdProductAndInstallationCode(
    clientId, product, productVersion, installationCode, repo, branch
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
                pc = pcrepo.findByLicenseIdProductAndInstallationCode(
                    license["id"],
                    product,
                    productVersion,
                    installationCode,
                    repo,
                    branch,
                )
                if pc:
                    return license
        else:
            print(f"No license found for clientId {clientId}")

    return None


def findByEmailProductAndInstallationCode(
    email, product, productVersion, installationCode, repo, branch
):
    client = clientrepo.findByEmail(email, repo, branch)
    if client:
        print(client)
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
                    pc = pcrepo.findByLicenseIdProductAndInstallationCode(
                        license["id"],
                        product,
                        productVersion,
                        installationCode,
                        repo,
                        branch,
                    )
                    if pc:
                        return license
            else:
                print(f"No license found for clientId {clientId}")
        else:
            print("No licenses found")
    else:
        print(f"No client found for email {email}")

    return None
