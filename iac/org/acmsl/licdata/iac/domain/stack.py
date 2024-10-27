# vim: set fileencoding=utf-8
"""
org/acmsl/licdata/iac/domain/stack.py

This script defines the Stack class.

Copyright (C) 2024-today acmsl's licdata

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
import abc
from pythoneda.shared import BaseObject, Port


class Stack(Port, BaseObject):
    """
    A Licdata infrastructure stack.

    Class name: Stack

    Responsibilities:
        - Represent a Licdata infrastructure stack.

    Collaborators:
        - org.acmsl.licdata.domain.LicdataIac
    """

    def __init__(self, name: str):
        """
        Creates a new stack instance.
        :param name: The name of the stack.
        :type name: str
        """
        super().__init__()
        self._name = name

    @property
    def name(self) -> str:
        """
        Retrieves the stack name.
        :return: The name of the stack.
        :rtype: str
        """
        return self._name

    @abc.abstractmethod
    async def up(self):
        """
        Brings up the stack.
        """
        pass


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
