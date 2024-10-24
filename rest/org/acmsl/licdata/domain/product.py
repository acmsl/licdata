"""
org/acmsl/licdata/domain/product.py

This file defines the Product class.

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

from pythoneda import Entity
from pythoneda.value_object import primary_key_attribute, attribute


class Product(Entity):
    """
    Represents a product.

    Class name: Product

    Responsibilities:
        - Represents something that can be purchased by a Client.

    Collaborators:
        - ProductType: Defines the type of a product.
    """

    def __init__(self, id, productTypeId: str, productVersion: str):
        """
        Creates a new Product instance.
        :param id: The id.
        :type id: str
        :param productTypeId: The id of the ProductType.
        :type productTypeId: str
        :param productVersion: The version of the product.
        :type productVersion: str
        """
        super().__init__(id)
        self._product_type_id = productTypeId
        self._product_version = productVersion

    @property
    @primary_key_attribute
    def product_type_id(self) -> str:
        """
        Retrieves the id of the product type.
        :return: Such information.
        :rtype: str
        """
        return self._product_type_id

    @property
    @primary_key_attribute
    def product_version(self) -> str:
        """
        Retrieves the product version.
        :return: Such information.
        :rtype: str
        """
        return self._product_version
