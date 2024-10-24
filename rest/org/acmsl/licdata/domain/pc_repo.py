"""
org/acmsl/licdata/domain/pc_repo.py

This file defines the PcRepo class.

Copyright (C) 2023-today ACM S.L. Licdata

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public Pc as published by
the Free Software Foundation, either version 3 of the Pc, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public Pc for more details.

You should have received a copy of the GNU General Public Pc
along with this program.  If not, see <https://www.gnu.org/pcs/>.
"""

from org.acmsl.licdata.domain import Pc
from pythoneda.shared import Repo


class PcRepo(Repo):
    """
    A subclass of Repo that manages Pcs.

    Class name: PcRepo

    Responsibilities:
        - Accesses and manages the persistence of Pc instances.

    Collaborators:
        - Pc: To provide metadata regarding the information to persist.

    """

    def __init__(self):
        """
        Creates a new PcRepo instance.
        """
        super().__init__(Pc)
