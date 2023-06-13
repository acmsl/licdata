"""
licdata/rest/domain/incident.py

This file defines the Incident class.

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
from pythoneda.value_object import primary_key_attribute


class Incident(Entity):
    """
    Represents a incident.

    Class name: Incident

    Responsibilities:
        - Contains relevant information about an incident.

    Collaborators:
        - License: Each incident is related to a license.
        - PC: Each incident is related to a PC.
    """

    def __init__(self, id: str, license_id: str, pc_id: str):
        """
        Creates a new Incident instance.
        :param id: The id.
        :type id: str
        :param license_id: The id of the license.
        :type license_id: str
        :param pc_id: The id of the PC.
        :type pc_id: str
        """
        super().__init__(id)
        self._license_id = license_id
        self._pc_id = pc_id


    @property
    @primary_key_attribute
    def license_id(self) -> str:
        """
        Retrieves the license id.
        :return: Such id.
        :rtype: str
        """
        return self._license_id


    @property
    @primary_key_attribute
    def pc_id(self) -> str:
        """
        Retrieves the PC id.
        :return: Such id.
        :rtype: str
        """
        return self._pc_id
