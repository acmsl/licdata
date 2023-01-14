import sys

sys.path.insert(0, "common")

from prelicenserepo import PrelicenseRepo
import common
import rest


def handler(event, context):

    return rest.create(
        event, context, common.retrievePk, common.retrieveAttributes, PrelicenseRepo(), "prelicenses"
    )
