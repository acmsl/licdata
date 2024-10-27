# vim: set fileencoding=utf-8
"""
org/acmsl/licdata/iac/infrastructure/pulumi_stack.py

This script defines the PulumiStack class.

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
from org.acmsl.licdata.iac.domain import Stack
from pulumi.automation import LocalWorkspace, create_or_select_stack


class PulumiStack(Stack, abc.ABC):
    """
    Pulumi implementation of Licdata infrastructure stacks.

    Class name: PulumiStack

    Responsibilities:
        - Use Pulumi stack as Licdata infrastructure stack.

    Collaborators:
        - org.acmsl.licdata.domain.Stack
    """

    def __init__(self, name: str):
        """
        Creates a new PulumiStack instance.
        :param name: The name of the stack.
        :type name: str
        """
        super().__init__(name)
        print(f"name -> {name}, {self.name}")

    async def up(self):
        """
        Brings up the stack.
        """
        workspace = LocalWorkspace()

        stack = create_or_select_stack(
            stack_name=self.name,
            project_name="licdata-iac",
            program=self.create_infrastructure,
        )

        outcome = await stack.up(on_output=self.__class__.logger().debug)

    @abc.abstractmethod
    async def create_infrastructure(self):
        """
        Creates the infrastructure.
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
