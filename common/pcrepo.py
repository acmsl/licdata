import json
from uuid import uuid4
import os
from github import Github


def findById(id):
    token = os.environ["GITHUB_TOKEN"]
    github = Github(token)
    repository = os.environ["GITHUB_REPO"]
    repo = github.get_repo(repository)
    branch = os.environ["GITHUB_BRANCH"]
    pc = None
    try:
        file = repo.get_contents(f"pcs/{id}/data.json", ref=branch)
    except:
        file = None
    if file:
        pc = json.loads(file.decoded_content.decode())
    return pc


def insert(
    licenses, product, productVersion, installationCode, pcDescription, repo, branch
):
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
        item["product"] = product
        item["productVersion"] = productVersion
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
            item["product"] = product
            item["productVersion"] = productVersion
            item["description"] = pcDescription
            repo.create_file(
                f"pcs/{result}/data.json",
                f"Created {result} pc",
                json.dumps(item),
                branch=branch,
            )

    return result


def addLicense(pcId, licenseId):
    token = os.environ["GITHUB_TOKEN"]
    github = Github(token)
    repository = os.environ["GITHUB_REPO"]
    repo = github.get_repo(repository)
    branch = os.environ["GITHUB_BRANCH"]
    try:
        pcFile = repo.get_contents(f"pcs/{pcId}/data.json", ref=branch)
    except:
        pcFile = None
    if pcFile:
        content = json.loads(pcFile.decoded_content.decode())
        content["licenses"].append(licenseId)
        content.append(item)
        repo.update_file(
            f"pcs/{pcId}/data.json",
            "acmsl-licdata",
            json.dumps(content),
            file.sha,
            branch=branch,
        )
    else:
        print(f"Cannot add license to non-existing pc {pcId}")


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
        allPcs = repo.get_contents("pcs/data.json", ref=branch)
    except:
        allPcs = None
    if allPcs:
        pcs = json.loads(allPcs.decoded_content.decode())
        pc = filterByProductAndInstallationCode(
            pcs, product, productVersion, installationCode, repo, branch
        )
        if pc and licenseId in pc["licenses"]:
            return pc
        else:
            print(f"No pc found for license {licenseId}")
    else:
        print("No pcs found")

    return None


def findByProductAndInstallationCode(
    product, productVersion, installationCode, repo, branch
):
    try:
        allPcs = repo.get_contents("pcs/data.json", ref=branch)
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