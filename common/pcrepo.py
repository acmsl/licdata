import json
from uuid import uuid4


def insert(product, productVersion, installationCode, pcDescription, repo, branch):
    result = str(uuid4())

    try:
        file = repo.get_contents("pcs.json", ref=branch)
    except:
        file = None
    if file is None:
        content = []
        item = {}
        item["id"] = result
        item["product"] = product
        item["productVersion"] = productVersion
        item["installationCode"] = installationCode
        item["description"] = pcDescription
        content.append(item)
        repo.create_file("pcs.json", "First PC", json.dumps(content), branch=branch)
    else:
        content = json.loads(file.decoded_content.decode())
        el = [x for x in content if x["installationCode"] == installationCode]
        if el:
            result = el[0]["id"]
        else:
            item = {}
            item["id"] = result
            item["product"] = product
            item["productVersion"] = productVersion
            item["installationCode"] = installationCode
            item["description"] = pcDescription
            content.append(item)
            repo.update_file(
                "pcs.json",
                "acmsl-licdata",
                json.dumps(content),
                file.sha,
                branch=branch,
            )

    return result


def filterByProductAndInstallationCode(
    items, product, productVersion, installationCode, repo, branch
):
    for pc in items:
        pcId = pc["id"]
        try:
            pcFile = repo.get_contents(f"pcs/{pcId}/data.json", ref=branch)
        except:
            pcFile = None
        if pcFile:
            pcContent = json.loads(pcFile.decoded_content.decode())
            if (
                pcContent["product"] == product
                and pcContent["productVersion"] == productVersion
                and pcContent["installationCode"] == installationCode
            ):
                return pcContent
        else:
            print(f"No pc file found at pcs/{pcId}/data.json")
    return None


def findByLicenseIdProductAndInstallationCode(
    licenseId, product, productVersion, installationCode, repo, branch
):
    pc = findByProductAndInstallationCode
    try:
        allPcs = repo.get_contents("pcs.json", ref=branch)
    except:
        allPcs = None
    if allPcs:
        allPcsContent = json.loads(allPcs.decoded_content.decode())
        pcs = [x for x in allPcsContent if licenseId in x["licenses"]]
        if pcs:
            pc = filterByProductAndInstallationCode(
                pcs, product, productVersion, installationCode, repo, branch
            )
            if pc:
                return pc

        else:
            print(f"No pc found for license {licenseId}")

    return None


def findByProductAndInstallationCode(
    product, productVersion, installationCode, repo, branch
):
    try:
        allPcs = repo.get_contents("pcs.json", ref=branch)
    except:
        allPcs = None
    if allPcs:
        allPcsContent = json.loads(allPcs.decoded_content.decode())
        if allPcsContent:
            return filterByProductAndInstallationCode(
                allPcsContent, product, productVersion, installationCode, repo, branch
            )
    else:
        print(f"No pcs found")

    return None
