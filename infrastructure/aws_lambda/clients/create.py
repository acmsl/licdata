import sys

sys.path.insert(0, "application")
sys.path.insert(0, "infrastructure/aws_lambda")
sys.path.insert(0, "domain")

from application import Licdata
import common
import rest
from client import Client

def handler(event, context):

    print(f"In clients/create.py#14")
    print(Client.primaryKey())
    return rest.create(
        event,
        context,
        common.retrievePk,
        common.retrieveAttributes,
        Licdata.clientRepo()
    )
