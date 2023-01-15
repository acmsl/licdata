import sys

sys.path.insert(0, "common")

from producttyperepo import ProductTypeRepo
import common
import rest


def handler(event, context):

    return rest.create(
        event, context, common.retrievePk, common.retrieveAttributes, ProductTypeRepo(), "product-types"
    )
