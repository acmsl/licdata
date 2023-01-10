import json

import githubrepo


def findById(id):
    return githubrepo.findById(id, "incidents")


def insert(licenseId, email, product, productVersion, installationCode):
    item = {}
    item["email"] = email
    item["product"] = product
    item["productVersion"] = productVersion
    item["installationCode"] = installationCode
    return githubrepo.insert(
        item,
        "incidents",
        ["licenseId", "email"],
        ["licenseId", "email", "product", "productVersion", "installationCode"],
    )


def update(id, licenseId, email, product, productVersion, installationCode):
    item = {}
    item["email"] = email
    item["product"] = product
    item["productVersion"] = productVersion
    item["installationCode"] = installationCode
    return githubrepo.update(
        item,
        "incidents",
        ["licenseId", "email"],
        ["licenseId", "email", "product", "productVersion", "installationCode"],
    )


def delete(id):
    return githubrepo.delete(id, "incidents")
