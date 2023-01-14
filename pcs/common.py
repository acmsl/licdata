import sys

sys.path.insert(0, "common")

from pcrepo import PcRepo
import rest
import params


def retrievePk(body, event):
    return [params.retrieveEmail(body, event)]


def retrieveAttributes(body, event):
    return rest.retrieveAttributesFromParams(body, event, PcRepo().attributes)
