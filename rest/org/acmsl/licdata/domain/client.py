"""
org/acmsl/licdata/domain/client.py

This file defines the Client class.

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


class Client(Entity):
    """
    Represents a client.

    Class name: Client

    Responsibilities:
        - Contains all relevant information about a client.

    Collaborators:
        - None

    """

    def __init__(self, id, email: str, address: str, contact: str, phone: str):
        """
        Creates a new Client instance.
        :param email: The email.
        :type email: str
        :param address: The address.
        :type address: str
        :param contact: The contact.
        :type contact: str
        :param phone: The phone.
        :type phone: str
        """
        super().__init__(id)
        self._email = email
        self._address = address
        self._contact = contact
        self._phone = phone

    @property
    @primary_key_attribute
    def email(self) -> str:
        """
        Retrieves the email.
        :return: Such email address.
        :rtype: str
        """
        return self._email

    @property
    @attribute
    def address(self) -> str:
        """
        Retrieves the address.
        :return: Such address.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, newAddress: str):
        """
        Specifies a new address.
        :param newAddress: Such address.
        :type newAddress: str
        """
        self._address = newAddress

    @property
    @attribute
    def contact(self) -> str:
        """
        Retrieves the contact.
        :return: Such contact.
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, newValue):
        """
        Specifies a new contact.
        :param newValue: Such contact.
        :type newValue: str
        """
        self._contact = newValue

    @property
    @attribute
    def phone(self):
        """
        Retrieves the phone.
        :return: Such phone.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, newValue):
        """
        Specifies a new phone.
        :param newValue: Such phone.
        :type newValue: str
        """
        self._phone = newValue
