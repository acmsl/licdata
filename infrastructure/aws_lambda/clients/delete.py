import sys
sys.path.insert(0, "domain")
sys.path.insert(0, "application")
sys.path.insert(0, "infrastructure/aws_lambda")
from licdata import Licdata
from client_repo import ClientRepo
import common
import rest


def handler(event, context):
    return rest.delete(event, context, Licdata.instance().get_repo(ClientRepo))
