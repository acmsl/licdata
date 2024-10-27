# vim: set fileencoding=utf-8
"""
org/acmsl/licdata/iac/infrastructure/azure/api_management_service.py

This script defines the ApiManagementService class.

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
import pulumi
import pulumi_azure_native


class ApiManagementService:
    """
    Azure ApiManagementService for Licdata.

    Class name: ApiManagementService

    Responsibilities:
        - Define the Azure Api Management Service for Licdata.

    Collaborators:
        - None
    """

    def __init__(self, resourceGroup: pulumi_azure_native.resources.ResourceGroup):
        """
        Creates a new ApiManagementService instance.
        :param resourceGroup: The ResourceGroup.
        :type resourceGroup: pulumi_azure_native.resources.ResourceGroup
        """
        super().__init__()
        self._api_management_service = self.create_api_managenent_service(
            "licenses",
            self.resource_group,
            "admin@example.com",
            "admin",
            "Consumption",
            0,
        )

    @property
    def api_management_service(
        self,
    ) -> pulumi_azure_native.apimanagement.ApiManagementService:
        """
        Retrieves the API Management Service.
        :return: Such API Management Service.
        :rtype: pulumi_azure_native.apimanagement.ApiManagementService
        """
        return self._api_management_service

    def deploy(self):
        """
        Deploys the infrastructure.
        """
        pulumi.export("api_management_service", self.api_management_service.name)


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
