import sys

sys.path.insert(0, "common")

from pcrepo import PcRepo
import rest


def handler(event, context):
    return rest.findById(event, context, PcRepo())
