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
        "prelicenses",
        common.retrieveFilterKeys(),
        common.retrieveAttributeNames(),
    )
