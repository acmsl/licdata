import sys
sys.path.insert(0, "common")

from orderrepo import OrderRepo
import common
import rest


def handler(event, context):
    return rest.update(
        event,
        context,
        common.retrieveAttributes,
        OrderRepo()
    )
