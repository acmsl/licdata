import sys
sys.path.insert(0, "domain")
sys.path.insert(0, "infrastructure/aws_lambda")
from order import Order
import rest


def retrieve_pk(body, event):
    return rest.retrieve_attributes_from_params(body, event, Order.primary_key())


def retrieve_attributes(body, event):
    return rest.retrieve_attributes_from_params(body, event, Order.attributes())
