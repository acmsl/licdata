import sys
sys.path.insert(0, "application")
sys.path.insert(0, "infrastructure/aws_lambda")
from licdata import Licdata
import common
import rest


def handler(event, context):
    return rest.list(event, context, Licdata.instance().listRepo)
