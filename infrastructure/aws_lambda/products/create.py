import sys

sys.path.insert(0, "common")

from productrepo import ProductRepo
import common
import rest


def handler(event, context):

    return rest.create(
        event, context, common.retrievePk, common.retrieveAttributes, ProductRepo(), "products"
    )
