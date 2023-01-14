import sys
sys.path.insert(0, "common")

from orderrepo import OrderRepo
import rest


def handler(event, context):
    return rest.findById(event, context, OrderRepo())
