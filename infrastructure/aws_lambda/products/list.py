import sys
sys.path.insert(0, "domain")
sys.path.insert(0, "application")
sys.path.insert(0, "infrastructure/aws_lambda")
from licdata import Licdata
from product_repo import ProductRepo
import common
import rest


def handler(event, context):
    return rest.list(event, context, Licdata.instance().get_repo(ProductRepo))
