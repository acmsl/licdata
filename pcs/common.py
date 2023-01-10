import sys

sys.path.insert(0, "common")

import pcrepo
import rest
import params


def findByPk(installationCode):
    return pcrepo.findByInstallationCode(installationCode)


def retrievePk(body, event):
    return params.retrieveInstallationCode(body, event)


def retrieveAttributes(body, event):
    return rest.retrieveAttributesFromParams(body, event, retrieveAttributeNames())


def retrieveFilterKeys():
    return ["installationCode"]


def retrieveAttributeNames():
    return (["licenses", "installationCode", "description"],)
