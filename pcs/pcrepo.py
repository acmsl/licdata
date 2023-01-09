import githubrepo


def findById(id):
    return githubrepo.findById(id, "pcs")


def findByLicenseIdAndInstallationCode(licenseId, installationCode):
    result = []
    filter = {}
    filter["installationCode"] = installationCode
    pcs = githubrepo.findAllByAttribute(installationCode, "installationCode", "pcs")
    if pcs:
        for pc in pcs:
            if pc and licenseId in pc.get("licenses"):
                result.append(pc)
            else:
                print(f"No pc found for license {licenseId}")
    else:
        print("No pcs found")

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


def findByInstallationCode(installationCode):
    return githubrepo.findByAttribute(installationCode, "installationCode", "pcs")


def addLicense(id, licenseId):
    result = None
    pc = findById(id)
    if pc:
        licenses = pc.get("licenses", [])
        if not licenseId in licenses:
            licenses.append(licenseId)
            pc["licenses"] = licenses
            result = update(
                pc,
                "pcs",
                ["installationCode"],
                ["licenses", "installationCode", "description"],
            )
    else:
        print(f"Cannot add license to non-existing pc {pcId}")

    return result


def insert(licenses, installationCode, pcDescription):
    item = {}
    item["installationCode"] = installationCode
    item["licenses"] = licenses
    item["description"] = pcDescription
    return githubrepo.insert(
        item,
        "pcs",
        ["installationCode"],
        ["licenses", "installationCode", "description"],
    )


def update(id, licenses, installationCode, pcDescription):
    item = {}
    item["id"] = id
    item["installationCode"] = installationCode
    item["licenses"] = licenses
    item["description"] = pcDescription
    return githubrepo.update(
        item,
        "pcs",
        ["installationCode"],
        ["licenses", "installationCode", "description"],
    )


def delete(id):
    return githubrepo.delete(id, "pcs")
