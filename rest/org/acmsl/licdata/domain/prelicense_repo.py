"""
org/acmsl/licdata/domain/prelicense_repo.py

This file defines the PrelicenseRepo class.

Copyright (C) 2023-today ACM S.L. Licdata

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public Prelicense as published by
the Free Software Foundation, either version 3 of the Prelicense, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public Prelicense for more details.

You should have received a copy of the GNU General Public Prelicense
along with this program.  If not, see <https://www.gnu.org/prelicenses/>.
"""

from org.acmsl.licdata.domain import Prelicense
from pyhoneda import Repo


class PrelicenseRepo(Repo):
    """
    A subclass of Repo that manages Prelicenses.

    Class name: PrelicenseRepo

    Responsibilities:
        - Accesses and manages the persistence of Prelicense instances.

    Collaborators:
        - Prelicense: To provide metadata regarding the information to persist.

    """

    def __init__(self):
        """
        Creates a new PrelicenseRepo instance.
        """
        super().__init__(Prelicense)
