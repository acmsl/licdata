import sys

sys.path.insert(0, "common")

import common
import rest


def handler(event, context):

    return rest.update(
        event,
        context,
        common.retrieveAttributes,
        "pcs",
        common.retrieveFilterKeys(),
        common.retrieveAttributeNames(),
    )
