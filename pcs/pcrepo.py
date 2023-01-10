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
