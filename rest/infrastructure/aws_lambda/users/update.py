import sys
sys.path.insert(0, "domain")
sys.path.insert(0, "application")
sys.path.insert(0, "infrastructure/aws_lambda")
from licdata import Licdata
from user_repo import UserRepo
import common
import rest


def handler(event, context):
    return rest.update(
        event,
        context,
        common.retrieve_attributes,
        Licdata.instance().get_repo(UserRepo))
