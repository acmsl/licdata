"""
org/acmsl/licdata/domain/pc.py

This file defines the PC class.

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


class Pc(Entity):
    """
    Represents a PC.

    Class name: Pc

    Responsibilities:
        - Contains details about a personal computer in which a product is installed.

    Collaborators:
        - None
    """

    def __init__(self, id: str, installationCode: str):
        """
        Creates a new Pc instance.
        :param id: The id.
        :type id: str
        :param installationCode: The installation code.
        :type installationCode: str
        """
        super().__init__(id)
        self._installation_code = installationCode

    @property
    @primary_key_attribute
    def installation_code(self) -> str:
        """
        Retrieves the installation code.
        :return: Such value.
        :rtype: str
        """
        return self._installation_code
