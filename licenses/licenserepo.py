import json

import githubrepo
import pcrepo
import clientrepo

import datetime


def findById(licenseId):
    repo = githubrepo.getRepo()
    branch = githubrepo.getBranch()
    license = None
    try:
        file = repo.get_contents(f"licenses/{licenseId}/data.json", ref=branch)
    except:
        file = None
    if file:
        license = json.loads(file.decoded_content.decode())
        license["licenseEnd"] = datetime.datetime.strptime(
            license.get("licenseEnd", "1970/01/01"), "%Y/%m/%d"
        )
    return license


def insert(clientId, product, productVersion):
    repo = githubrepo.getRepo()
    branch = githubrepo.getBranch()
    result = githubrepo.newId()

    now = datetime.datetime.now()
    orderDate = now.strftime("%Y/%m/%d")
    deliveryDate = orderDate
    licenseType = ""
    licenseEnd = (now + datetime.timedelta(days=2)).strftime("%Y/%m/%d")
    item = {}
    item["id"] = result
    item["clientId"] = clientId
    item["product"] = product
    item["productVersion"] = productVersion

    try:
        file = repo.get_contents("licenses/data.json", ref=branch)
    except:
        file = None
    if file is None:
        now = datetime.datetime.now()
        content = []
        content.append(item)
        repo.create_file(
            "licenses/data.json", "First license", json.dumps(content), branch=branch
        )
    else:
        content = json.loads(file.decoded_content.decode())
        content.append(item)
        repo.update_file(
            "licenses/data.json",
            "acmsl-licdata",
            json.dumps(content),
            file.sha,
            branch=branch,
        )

    item["orderDate"] = orderDate
    item["deliveryDate"] = deliveryDate
    item["licenseType"] = licenseType
    item["licenseEnd"] = licenseEnd
    repo.create_file(
        f"licenses/{result}/data.json",
        f"Created {result} license",
        json.dumps(item),
        branch=branch,
    )
    return result


def findByClientIdAndInstallationCode(clientId, installationCode):
    repo = githubrepo.getRepo()
    branch = githubrepo.getBranch()
    try:
        allLicenses = repo.get_contents("licenses/data.json", ref=branch)
    except:
        allLicenses = None
    if allLicenses:
        allLicensesContent = json.loads(allLicenses.decoded_content.decode())
        licenses = [x for x in allLicensesContent if x["clientId"] == clientId]
        if licenses:
            for license in licenses:
                pc = pcrepo.findByLicenseIdAndInstallationCode(
                    license["id"], installationCode
                )
                if pc:
                    return license
        else:
            print(f"No license found for clientId {clientId}")

    return None


def findByEmailProductAndInstallationCode(
    email, product, productVersion, installationCode
):
    repo = githubrepo.getRepo()
    branch = githubrepo.getBranch()
    client = clientrepo.findByEmail(email)
    if client:
        print(client)
        clientId = client.get("id", "missing")
        try:
            allLicenses = repo.get_contents("licenses/data.json", ref=branch)
        except:
            allLicenses = None
        if allLicenses:
            allLicensesContent = json.loads(allLicenses.decoded_content.decode())
            licenses = [
                x
                for x in allLicensesContent
                if x["clientId"] == clientId
                and x["product"] == product
                and x["productVersion"] == productVersion
            ]
            if licenses:
                for license in licenses:
                    pc = pcrepo.findByLicenseIdAndInstallationCode(
                        license["id"], installationCode
                    )
                    if pc:
                        return findById(license["id"])
            else:
                print(f"No licenses found for clientId {clientId}")
        else:
            print("No licenses found")
    else:
        print(f"No client found for email {email}")

    return None
