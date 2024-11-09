# vim: set fileencoding=utf-8
"""
org/acmsl/licdata/infrastructure/azure/clients/create.py

This file defines the Create-Client script for Azure.

Copyright (C) 2024-today acm-sl's licdata

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
import azure.functions as func
from org.acmsl.licdata.application import LicdataApp
from org.acmsl.licdata.domain.events import NewClientRequested
import org.acmsl.licdata.infrastructure.clients.common
import org.acmsl.licdata.infrastructure.rest
from typing import Dict


async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    """
    Receives an HTTP POST request to create a new client.
    :param req: The HTTP request.
    :type req: azure.functions.HttpRequest
    :param context: The context.
    :type context: azure.functions.Context
    :return: The HTTP response.
    :rtype: azure.functions.HttpResponse
    """
    event = NewClientRequested(
        req.params.get("email"),
        req.params.get("address"),
        req.params.get("contact"),
        req.params.get("phone"),
    )
    print(f"Before calling accept_new_client_requested")
    created = await LicdataApp.instance().accept_new_client_requested(event)
    return func.HttpResponse(f"Client created: {created}")


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
