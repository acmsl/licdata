import sys
sys.path.insert(0, "application")
sys.path.insert(0, "infrastructure/aws_lambda")
from licdata import Licdata
import common
import rest

def handler(event, context):

    return rest.create(
        event,
        context,
        common.retrieve_pk,
        common.retrieve_attributes,
        Licdata.instance().orderRepo)
