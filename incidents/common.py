import sys

sys.path.insert(0, "common")

from incidentrepo import IncidentRepo
import rest
import params


def retrievePk(body, event):
    return [ params.retrieveId(body, event) ]


def retrieveAttributes(body, event):
    return rest.retrieveAttributesFromParams(body, event, IncidentRepo().attributes)
