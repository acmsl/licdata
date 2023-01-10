import sys

sys.path.insert(0, "common")

import common
import rest
from cryptography.fernet import Fernet


def handler(event, context):

    print(Fernet.generate_key())

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
