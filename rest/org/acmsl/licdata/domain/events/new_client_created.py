#!/usr/bin/env python3
"""
org/acmsl/licdata/domain/events/new_client_created.py

This file defines the NewClientCreated class.

Copyright (C) 2024-today ACM S.L. Licdata

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
from pythoneda.shared import Event
from typing import List


class NewClientCreated(Event):
    """
    Represents events for creating new Client instances.

    Class name: NewClientCreated

    Responsibilities:
        - Represent the event when a new Client has been created.

    Collaborators:
        - None
    """

    def __init__(
        self,
        email: str,
        address: str,
        contact: str,
        phone: str,
        previousEventIds: List[str] = None,
        reconstructedId: str = None,
        reconstructedPreviousEventIds: List[str] = None,
    ):
        """
        Creates a new NewClientCreated instance.
        :param email: The email.
        :type email: str
        :param address: The address.
        :type address: str
        :param contact: The contact information.
        :type contact: str
        :param phone: The phone.
        :type phone: str
        """
        super().__init__(
            previousEventIds, reconstructedId, reconstructedPreviousEventIds
        )
        self._email = email
        self._address = address
        self._contact = contact
        self._phone = phone

    @property
    def email(self) -> str:
        """
        Retrieves the email.
        :return: Such email.
        :rtype: str
        """
        return self._email

    @property
    def address(self) -> str:
        """
        Retrieves the address.
        :return: Such address.
        :rtype: str
        """
        return self._address

    @property
    def contact(self) -> str:
        """
        Retrieves the contact.
        :return: Such contact.
        :rtype: str
        """
        return self._contact

    @property
    def phone(self) -> str:
        """
        Retrieves the phone.
        :return: Such phone.
        :rtype: str
        """
        return self._phone


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
