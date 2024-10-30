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
from .function_storage_account import FunctionStorageAccount
from .app_service_plan import AppServicePlan
from .function_app import FunctionApp
from .dns_zone import DnsZone
from .dns_record import DnsRecord
from .front_door import FrontDoor
from .frontend_endpoint import FrontendEndpoint


class PulumiAzureStack(PulumiStack):
    """
    Azure-specific Pulumi implementation of Licdata infrastructure stacks.

    Class name: PulumiAzureStack

    Responsibilities:
        - Use Azure-specific Pulumi stack as Licdata infrastructure stack.

    Collaborators:
        - org.acmsl.licdata.infrastructure.PulumiStack
    """

    def __init__(self, name: str, projectName: str):
        """
        Creates a new PulumiAzureStack instance.
        :param name: The name of the stack.
        :type name: str
        :param projectName: The name of the project.
        :type projectName: str
        """
        super().__init__(name, projectName)
        self._resource_group = None
        self._function_storage_account = None
        self._app_service_plan = None
        self._function_app = None
        self._dns_zone = None
        self._dns_record = None
        self._front_door = None
        self._frontend_endpoint = None

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

    @property
    def function_storage_account(self) -> FunctionStorageAccount:
        """
        Retrieves the Azure Function Storage Account.
        :return: Such Function Storage Account.
        :rtype: FunctionStorageAccount
        """
        return self._function_storage_account

    @property
    def app_service_plan(self) -> AppServicePlan:
        """
        Retrieves the Azure App Service Plan.
        :return: Such App Service Plan.
        :rtype: AppServicePlan
        """
        return self._app_service_plan

    @property
    def function_app(self) -> FunctionApp:
        """
        Retrieves the Azure Function App.
        :return: Such Function App.
        :rtype: FunctionApp
        """
        return self._function_app

    @property
    def dns_zone(self) -> DnsZone:
        """
        Retrieves the Azure DNS Zone.
        :return: Such DNS Zone.
        :rtype: DnsZone
        """
        return self._dns_zone

    @property
    def dns_record(self) -> DnsRecord:
        """
        Retrieves the Azure DNS Record.
        :return: Such DNS Record.
        :rtype: DnsRecord
        """
        return self._dns_record

    @property
    def front_door(self) -> FrontDoor:
        """
        Retrieves the Azure Front Door.
        :return: Such Front Door.
        :rtype: FrontDoor
        """
        return self._front_door

    @property
    def frontend_endpoint(self) -> FrontendEndpoint:
        """
        Retrieves the Azure Frontend Endpoint.
        :return: Such Frontend Endpoint.
        :rtype: FrontendEndpoint
        """
        return self._frontend_endpoint

    def declare_infrastructure(self):
        """
        Creates the infrastructure.
        """
        self._resource_group = ResourceGroup()
        self._function_storage_account = FunctionStorageAccount(self._resource_group)
        self._app_service_plan = AppServicePlan(self._resource_group)
        self._function_app = FunctionApp(
            self._function_storage_account, self._app_service_plan, self._resource_group
        )
        self._dns_zone = DnsZone(self._resource_group)
        # self._dns_record = DnsRecord(
        #    self._function_app.default_host_name.apply(lambda name: name),
        #    self._dns_zone,
        #    self._resource_group,
        # )
        # self._front_door = FrontDoor(self._resource_group)
        # self._frontend_endpoint = FrontendEndpoint(
        #     self._front_door, self._dns_record, self._dns_zone, self._resource_group
        # )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
