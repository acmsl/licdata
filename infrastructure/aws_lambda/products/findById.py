import sys

sys.path.insert(0, "common")

from productrepo import ProductRepo
import rest


def handler(event, context):
    return rest.findById(event, context, ProductRepo())
