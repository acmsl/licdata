import sys
sys.path.insert(0, "common")

from incidentrepo import IncidentRepo
import rest


def handler(event, context):
    return rest.findById(event, context, IncidentRepo())
