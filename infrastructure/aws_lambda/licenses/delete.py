import sys

sys.path.insert(0, "common")

from licenserepo import LicenseRepo
import rest


def handler(event, context):
    return rest.delete(event, context, LicenseRepo())
