import sys

sys.path.insert(0, "common")

import common
import rest


def handler(event, context):

    return rest.create(
        event,
        context,
        common.retrievePk,
        common.retrieveAttributes,
        common.findByPk,
        "clients",
        common.retrieveFilterKeys(),
        common.retrieveAttributeNames(),
    )
