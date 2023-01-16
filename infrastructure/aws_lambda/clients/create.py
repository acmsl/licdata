import sys

sys.path.insert(0, "application")
sys.path.insert(0, "infrastructure/aws_lambda")
sys.path.insert(0, "domain")

from application import Licdata
import common
import rest
from client import Client

def handler(event, context):

    return rest.create(
        event,
        context,
        common.retrieve_pk,
        common.retrieve_attributes,
        Licdata.clientRepo()
    )
