# vim: set fileencoding=utf-8
"""
org/acmsl/licdata/iac/azure/resource_group.py

This script defines the Azure ResourceGroup resources for Licdata.

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
# Import Pulumi Azure SDK
import pulumi
import pulumi_azure_native


class ResourceGroup:
    """
    Azure ResourceGroup resources for Licdata.

    Class name: ResourceGroup

    Responsibilities:
        - Define the Azure ResourceGroup resources.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new Azure instance.
        """
        super().__init__()
        self._resource_group = self.create_resource_group("licenses")

    @property
    def resource_group(self) -> pulumi_azure_native.resources.ResourceGroup:
        """
        Retrieves the Azure Resource Group.
        :return: Such Resource Group.
        :rtype: pulumi_azure_native.resources.ResourceGroup
        """
        return self._resource_group

    def create_resource_group(
        self, resourceGroupName: str
    ) -> pulumi_azure_native.resources.ResourceGroup:
        """
        Creates an Azure Resource Group.
        :param resourceGroupName: The name of the resource group.
        :type resourceGroupName: str
        :return: The Azure Resource Group.
        :rtype: pulumi_azure_native.resources.ResourceGroup
        """
        return pulumi_azure_native.resources.ResourceGroup(resourceGroupName)

    def deploy(self):
        """
        Deploys the infrastructure.
        """
        pulumi.export("resource_group", self.resource_group.name)


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
