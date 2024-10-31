# vim: set fileencoding=utf-8
"""
org/acmsl/licdata/infrastructure/aws_lambda/__init__.py

This file ensures org.acmsl.licdata.infrastructure.aws_lambda is a package.

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
__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from .mail import send_email, handler

from .params import (
    load_body,
    retrieve_param,
    retrieve_id,
    retrieve_client_id,
    retrieve_installation_code,
    retrieve_product,
    retrieve_product_version,
    retrieve_description,
    retrieve_duration,
    retrieve_bundle,
    retrieve_email,
    retrieve_address,
    retrieve_contact,
    retrieve_phone,
)

from .resp import build_response

from .rest import (
    retrieve_attributes_from_params,
    find_by_id,
    create,
    update,
    delete,
    list,
)


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End: