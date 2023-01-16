import sys
sys.path.insert(0, "common")
from client_repo import ClientRepo
import rest


def handler(event, context):
    return rest.delete(event, context, ClientRepo())
