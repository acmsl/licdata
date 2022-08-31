import json
from uuid import uuid4


def findById(pcId, repo, branch):
    pc = None
    try:
        file = repo.get_contents(f"pc/{pcId}/data.json", ref=branch)
    except:
        file = None
    if file:
        pc = json.loads(file.decoded_content.decode())
    return pc


def insert(licenses, installationCode, pcDescription, repo, branch):
    result = str(uuid4())

    item = {}
    item["id"] = result
    item["installationCode"] = installationCode

    try:
        file = repo.get_contents("pcs/data.json", ref=branch)
    except:
        file = None
    if file is None:
        content = []
        content.append(item)
        repo.create_file(
            "pcs/data.json", "First PC", json.dumps(content), branch=branch
        )
        item["licenses"] = licenses
        item["description"] = pcDescription
        repo.create_file(
            f"pcs/{result}/data.json",
            f"Created {result} pc",
            json.dumps(item),
            branch=branch,
        )
    else:
        content = json.loads(file.decoded_content.decode())
        el = [x for x in content if x["installationCode"] == installationCode]
        if el:
            result = el[0]["id"]
        else:
            content.append(item)
            repo.update_file(
                "pcs/data.json",
                "acmsl-licdata",
                json.dumps(content),
                file.sha,
                branch=branch,
            )
            item["licenses"] = licenses
            item["description"] = pcDescription
            repo.create_file(
                f"pcs/{result}/data.json",
                f"Created {result} pc",
                json.dumps(item),
                branch=branch,
            )

    return result


def addLicense(pcId, licenseId, repo, branch):
    try:
        file = repo.get_contents(f"pcs/{pcId}/data.json", ref=branch)
    except:
        file = None
    if file:
        content = json.loads(file.decoded_content.decode())
        content["licenses"].append(licenseId)
        repo.update_file(
            f"pcs/{pcId}/data.json",
            "acmsl-licdata",
            json.dumps(content),
            file.sha,
            branch=branch,
        )
    else:
        print(f"Cannot add license to non-existing pc {pcId}")


def filterByInstallationCode(items, installationCode, repo, branch):
    for pc in items:
        pcId = pc["id"]
        try:
            file = repo.get_contents(f"pcs/{pcId}/data.json", ref=branch)
        except:
            file = None
        if file:
            content = json.loads(file.decoded_content.decode())
            if content["installationCode"] == installationCode:
                return content
        else:
            print(f"No pc file found at pcs/{pcId}/data.json")

    return None


def findByLicenseIdAndInstallationCode(licenseId, installationCode, repo, branch):
    try:
        allPcs = repo.get_contents("pcs/data.json", ref=branch)
    except:
        allPcs = None
    if allPcs:
        pcs = json.loads(allPcs.decoded_content.decode())
        pc = filterByInstallationCode(pcs, installationCode, repo, branch)
        if pc and licenseId in pc["licenses"]:
            return pc
        else:
            print(f"No pc found for license {licenseId}")
    else:
        print("No pcs found")

    return None


def findByInstallationCode(installationCode, repo, branch):
    try:
        allPcs = repo.get_contents("pcs/data.json", ref=branch)
    except:
        allPcs = None
    if allPcs:
        allPcsContent = json.loads(allPcs.decoded_content.decode())
        if allPcsContent:
            return filterByInstallationCode(
                allPcsContent, installationCode, repo, branch
            )
    else:
        print(f"No pcs found")

    return None
