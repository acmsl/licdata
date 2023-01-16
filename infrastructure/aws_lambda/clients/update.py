import sys
sys.path.insert(0, "common")

from client_repo import ClientRepo
import common
import rest


def handler(event, context):
    return rest.update(
        event,
        context,
        common.retrieve_attributes,
        ClientRepo()
    )
