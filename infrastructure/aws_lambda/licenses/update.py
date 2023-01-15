import sys
sys.path.insert(0, "common")

from licenserepo import LicenseRepo
import common
import rest


def handler(event, context):
    return rest.update(
        event,
        context,
        common.retrieveAttributes,
        LicenseRepo()
    )
