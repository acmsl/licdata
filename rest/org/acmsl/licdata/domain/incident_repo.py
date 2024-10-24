"""
org/acmsl/licdata/domain/incident_repo.py

This file defines the IncidentRepo class.

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

from org.acmsl.licdata.domain import Incident
from pyhoneda import Repo


class IncidentRepo(Repo):
    """
    A subclass of Repo that manages Incidents.

    Class name: IncidentRepo

    Responsibilities:
        - Accesses and manages the persistence of Incident instances.

    Collaborators:
        - Incident: To provide metadata regarding the information to persist.

    """

    def __init__(self):
        """
        Creates a new IncidentRepo instance.
        """
        super().__init__(Incident)
