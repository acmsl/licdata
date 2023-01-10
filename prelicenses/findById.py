import sys

sys.path.insert(0, "common")
import rest


def handler(event, context):

    return rest.findById(event, context, "prelicenses")
