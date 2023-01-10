import json

import githubrepo
import pcrepo
import clientrepo

import datetime


def findById(licenseId):
    return githubrepo.findById(licenseId, "licenses")


def findByClientIdAndInstallationCode(clientId, installationCode):
    result = []
    licenses = githubrepo.findAllByAttribute(clientId, "clientId", "licenses")
    if licenses:
        for license in licenses:
            pc = pcrepo.findByLicenseIdAndInstallationCode(
                license["id"], installationCode
            )
            if pc:
                result.append(license)

    return result


def findByEmailProductAndInstallationCode(
    email, product, productVersion, installationCode
):
    result = []
    filter = {}
    filter["clientId"] = clientId
    filter["product"] = product
    filter["productVersion"] = productVersion
    licenses = githubrepo.findAllsByAttributes(filter, "licenses")
    if licenses:
        for license in licenses:
            licenseId = license.get("id")
            pc = pcrepo.findByLicenseIdAndInstallationCode(licenseId, installationCode)
            if pc:
                result.append(findById(licenseId))
            else:
                print(
                    f"WARNING: No pc found for license {licenseId} and installation code {installationCode}"
                )
    else:
        print(f"No client found for email {email}, product {product} {productVersion}")

    return result


def insert(clientId, product, productVersion):
    now = datetime.datetime.now()
    orderDate = now.strftime("%Y/%m/%d")
    deliveryDate = orderDate
    licenseType = ""
    licenseEnd = (now + datetime.timedelta(days=2)).strftime("%Y/%m/%d")
    item = {}
    item["product"] = product
    item["productVersion"] = productVersion
    item["licenseEnd"] = licenseEnd
    item["orderDate"] = orderDate
    item["deliveryDate"] = deliveryDate
    return githubrepo.insert(
        item,
        "licenses",
        ["clientId"],
        [
            "clientId",
            "product",
            "productVersion",
            "licenseEnd",
            "orderDate",
            "deliveryDate",
        ],
    )


def update(id, clientId, product, productVersion, licenseEnd, orderDate, deliveryDate):
    item = {}
    item["id"] = id
    item["clientId"] = clientId
    item["product"] = product
    item["productVersion"] = productVersion
    item["licenseEnd"] = licenseEnd
    item["orderDate"] = orderDate
    item["deliveryDate"] = deliveryDate
    return githubrepo.update(
        item,
        "licenses",
        ["clientId"],
        [
            "clientId",
            "product",
            "productVersion",
            "licenseEnd",
            "orderDate",
            "deliveryDate",
        ],
    )


def delete(id):
    return githubrepo.delete(id, "licenses")
