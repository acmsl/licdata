import sys

sys.path.insert(0, "common")

from licenserepo import LicenseRepo
import rest
import params


def retrievePk(body, event):
    return [ ]


def retrieveAttributes(body, event):
    return rest.retrieveAttributesFromParams(body, event, LicenseRepo().attributes)
