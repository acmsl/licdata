import sys
sys.path.insert(0, "common")

from clientrepo import ClientRepo
import rest


def handler(event, context):
    return rest.list(event, context, ClientRepo())
