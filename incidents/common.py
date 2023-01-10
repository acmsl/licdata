import sys

sys.path.insert(0, "common")

import rest
import params


def findByPk(pk):
    return None


def retrievePk(body, event):
    return None


def retrieveAttributes(body, event):
    return rest.retrieveAttributesFromParams(body, event, retrieveAttributeNames())


def retrieveFilterKeys():
    return ["licenseId", "email"]


def retrieveAttributeNames():
    return ["licenseId", "email", "product", "productVersion", "installationCode"]
