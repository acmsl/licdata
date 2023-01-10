import sys

sys.path.insert(0, "common")

import clientrepo
import rest
import params


def findByPk(email):
    return clientrepo.findByEmail(email)


def retrievePk(body, event):
    return params.retrieveEmail(body, event)


def retrieveAttributes(body, event):
    return rest.retrieveAttributesFromParams(body, event, retrieveAttributeNames())


def retrieveFilterKeys():
    return ["email"]


def retrieveAttributeNames():
    return ["email", "address", "contact", "phone"]
