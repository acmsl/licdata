# vim: set fileencoding=utf-8
"""
org/acmsl/licdata/iac/domain/licdata_iac.py

This script defines the LicdataIac class.

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
from .infrastructure_update_requested import InfrastructureUpdateRequested
from .infrastructure_updated import InfrastructureUpdated
from .stack_factory import StackFactory
from pythoneda.shared import EventListener, listen, Ports


class LicdataIac(EventListener):
    """
    Licdata Infrastructure as Code.

    Class name: LicdataIac

    Responsibilities:
        - Define the Licdata Infrastructure.

    Collaborators:
        - org.acmsl.licdata.domain.serverless.License
    """

    def __init__(self):
        """
        Creates a new LicdataIac instance.
        """
        super().__init__()

    @classmethod
    def instance(cls):
        """
        Retrieves the singleton instance.
        :return: Such instance.
        :rtype: org.acmsl.licdata.iac.domain.LicdataIac
        """
        if cls._singleton is None:
            cls._singleton = cls.initialize()

        return cls._singleton

    @classmethod
    @listen(InfrastructureUpdateRequested)
    async def listen_InfrastructureUpdateRequested(
        self, event: InfrastructureUpdateRequested
    ) -> InfrastructureUpdated:
        """
        Gets notified of a InfrastructureUpdateRequested event.
        :param event: The event.
        :type event: org.acmsl.licdata.iac.domain.InfrastructureUpdateRequested
        """
        print("InfrastructureUpdateRequested event received")
        factory = Ports.instance().resolve_first(StackFactory)
        stack = factory.new("dev")  # event.stack_name)
        await stack.up()


if __name__ == "__main__":
    asyncio.run(LicdataIacApp.main("org.acmsl.licdata.iac.application.LicdataIacApp"))
# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
