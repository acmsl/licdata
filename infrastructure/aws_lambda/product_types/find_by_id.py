import sys
sys.path.insert(0, "domain")
sys.path.insert(0, "application")
sys.path.insert(0, "infrastructure/aws_lambda")
from licdata import Licdata
from product_types_repo import ProductTypeRepo
import common
import rest


def handler(event, context):
    return rest.find_by_id(event, context, Licdata.instance().get_repo(ProductTypeRepo))
