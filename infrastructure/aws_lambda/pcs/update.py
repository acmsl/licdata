import sys

sys.path.insert(0, "common")

from pcrepo import PcRepo
import common
import rest


def handler(event, context):
    return rest.update(event, context, common.retrieveAttributes, PcRepo())
