import sys

sys.path.insert(0, "common")

from orderrepo import OrderRepo
import rest
import params


def retrievePk(body, event):
    return [ params.retrieveEmail(body, event) ]


def retrieveAttributes(body, event):
    return rest.retrieveAttributesFromParams(body, event, OrderRepo().attributes)
