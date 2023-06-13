"""
licdata/rest/domain/user_repo.py

This file defines the UserRepo class.

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
from domain.user import User
from pyhoneda.repo import Repo


class UserRepo(Repo):
    """
    A subclass of Repo that manages Users.

    Class name: UserRepo

    Responsibilities:
        - Accesses and manages the persistence of User instances.

    Collaborators:
        - User: To provide metadata regarding the information to persist.

    """
    def __init__(self):
        """
        Creates a new UserRepo instance.
        """
        super().__init__(User)
