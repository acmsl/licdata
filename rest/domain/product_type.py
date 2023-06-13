"""
licdata/rest/domain/product_type.py

This file defines the ProductType class.

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
from pythoneda.entity import Entity
from pythoneda.value_object import primary_key_attribute, attribute


class ProductType(Entity):
    """
    Represents a product type.

    Class name: ProductType

    Responsibilities:
        - Contains metadata shared by a group of products.

    Collaborators:
        - None
    """
    def __init__(self, id: str, name: str, version: str):
        """
        Creates a new ProductType instance.
        :param id: The id.
        :type id: str
        :param name: The name.
        :type name: str
        :param version: The version.
        :type version: str
        """
        super().__init__(id)
        self._name = name
        self._version = version


    @property
    @primary_key_attribute
    def name(self) -> str:
        """
        Retrieves the name.
        :return: Such information.
        :rtype: str
        """
        return self._name


    @property
    @primary_key_attribute
    def version(self):
        """
        Retrieves the version.
        :return: Such information.
        :rtype: str
        """
        return self._version
