import sys

sys.path.insert(0, "common")

import common
import rest
import params


def handler(event, context):

    return rest.create(
        event,
        context,
        common.retrievePk,
        common.retrieveAttributes,
        findByPk,
        "pcs",
        common.retrieveFilterKeys(),
        common.retrieveAttributeNames(),
    )
