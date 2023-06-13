"""
licdata/rest/infrastructure/aws_lambda/product_types/find_by_id.py

This file provides an AWS Lambda handler to find product types by id.

Copyright (C) 2023-today ACM S.L. Licdata

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from application.licdata import Licdata
from domain.product_type_repo import ProductTypeRepo
import infrastructure.aws_lambda.clients.common
import infrastructure.aws_lambda.rest

from typing import Dict

def handler(event, context) -> Dict:
    """
    AWS Lambda handler to find product types by id.
    :param event: The AWS Lambda event.
    :type event: event
    :param context: The AWS Lambda context.
    :type context: context
    :return: The response.
    :rtype: Dict
    """
    return rest.find_by_id(event, context, Licdata.instance().get_repo(ProductTypeRepo))
