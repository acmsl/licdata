#!/usr/bin/env python3
"""
org/acmsl/licdata/application/licdata.py

This file runs Licdata server.

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
from pythoneda.shared.application import PythonEDA

import asyncio


class Licdata(PythonEDA):
    """
    Runs Licdata server.

    Class name: Licdata

    Responsibilities:
        - Launch Licdata server from the command line

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new instance.
        """
        super().__init__()


if __name__ == "__main__":
    asyncio.run(Licdata.main())
