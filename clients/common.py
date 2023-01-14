import sys

sys.path.insert(0, "common")

from clientrepo import ClientRepo
import rest
import params


def retrievePk(body, event):
    return [ params.retrieveEmail(body, event) ]


def retrieveAttributes(body, event):
    return rest.retrieveAttributesFromParams(body, event, ClientRepo().attributes)
