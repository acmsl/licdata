import sys
sys.path.insert(0, "domain")
sys.path.insert(0, "infrastructure/aws_lambda")
from product import Product
import rest


def retrieve_pk(body, event):
    return rest.retrieve_attributes_from_params(body, event, Product.primary_key())


def retrieve_attributes(body, event):
    return rest.retrieve_attributes_from_params(body, event, Product.attributes())
