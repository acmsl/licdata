import sys

sys.path.insert(0, "common")

from prelicenserepo import PrelicenseRepo
import rest


def handler(event, context):
    return rest.delete(event, context, PrelicenseRepo())
