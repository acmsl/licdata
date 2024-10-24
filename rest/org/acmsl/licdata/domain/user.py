"""
org/acmsl/licdata/domain/user.py

This file defines the User class.

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


class User(Entity):
    """
    Represents an user.

    Class name: User

    Responsibilities:
        - Contains metadata about an user.

    Collaborators:
        - None
    """

    def __init__(self, id: str, email: str, password: str):
        """
        Creates a new User instance.
        :param id: The id.
        :type id: str
        :param email: The email.
        :type email: str
        :param password: The password
        :type password: str
        """
        super().__init__(id)
        self._email = email
        self._password = password

    @property
    @filter_attribute
    def email(self) -> str:
        """
        Retrieves the email.
        :return: Such value.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, newValue: str):
        """
        Specifies a new email.
        :param newValue: The new email address.
        :type newValue: str
        """
        self._email = newValue

    @property
    @encrypted_attribute
    def password(self) -> str:
        """
        Retrieves the password.
        :return: Such value.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, newValue):
        """
        Specifies a new password.
        :param newValue: The new password.
        :type newValue: str
        """
        self._password = newValue
