import sys

sys.path.insert(0, "common")

from producttyperepo import ProductTypeRepo
import rest


def handler(event, context):
    return rest.findById(event, context, ProductTypeRepo())
