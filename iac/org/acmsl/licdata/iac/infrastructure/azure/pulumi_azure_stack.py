# vim: set fileencoding=utf-8
"""
org/acmsl/licdata/iac/infrastructure/azure/pulumi_azure_stack.py

This script defines the PulumiAzureStack class.

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
from org.acmsl.licdata.iac.infrastructure import PulumiStack
from .resource_group import ResourceGroup


class PulumiAzureStack(PulumiStack):
    """
    Azure-specific Pulumi implementation of Licdata infrastructure stacks.

    Class name: PulumiStack

    Responsibilities:
        - Use Azure-specific Pulumi stack as Licdata infrastructure stack.

    Collaborators:
        - org.acmsl.licdata.infrastructure.PulumiStack
    """

    def __init__(self, name: str):
        """
        Creates a new PulumiAzureStack instance.
        :param name: The name of the stack.
        :type name: str
        """
        super().__init__(name)
        self._resource_group = None

    @classmethod
    def instantiate(cls):
        """
        Creates an instance.
        :return: The new instance.
        :rtype: org.acmsl.licdata.iac.infrastructure.azure.PulumiAzureStackFactory
        """
        raise InvalidOperationError("Cannot instantiate PulumiAzureStack directly")

    @property
    def resource_group(self) -> ResourceGroup:
        """
        Retrieves the Azure Resource Group.
        :return: Such Resource Group.
        :rtype: ResourceGroup
        """
        return self._resource_group

    async def create_infrastructure(self):
        """
        Creates the infrastructure.
        """
        self._resource_group = ResourceGroup()


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
