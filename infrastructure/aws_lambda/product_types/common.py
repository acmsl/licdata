import sys
sys.path.insert(0, "domain")
sys.path.insert(0, "infrastructure/aws_lambda")
from product_type import ProductType
import rest


def retrieve_pk(body, event):
    return rest.retrieve_attributes_from_params(body, event, ProductType.primary_key())


def retrieve_attributes(body, event):
    return rest.retrieve_attributes_from_params(body, event, ProductType.attributes())
