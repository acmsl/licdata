import sys
sys.path.insert(0, "common")

from clientrepo import ClientRepo
import common
import rest


def handler(event, context):
    return rest.update(
        event,
        context,
        common.retrieveAttributes,
        ClientRepo()
    )
