"""
org/acmsl/licdata/domain/order.py

This file defines the Order class.

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

from pythoneda.shared import Entity, primary_key_attribute, attribute


class Order(Entity):
    """
    Represents an order.

    Class name: Order

    Responsibilities:
        - Represents a purchase of a Client.

    Collaborators:
        - Client: An order belongs to a Client.
        - Product: An order contains a Product.
    """

    def __init__(
        self, id: str, clientId: str, productId: str, duration: int, orderDate
    ):
        """
        Creates a new Order instance.
        :param clientId: The id of the client.
        :type clientId: str
        :param productId: The id of the product.
        :type productId: str
        :param duration: The duration.
        :type duration: int
        :param orderDate: When the order was placed.
        :type orderDate: date
        """
        super().__init__(id)
        self._client_id = clientId
        self._product_id = productId
        self._duration = duration
        self._order_date = orderDate

    @property
    @primary_key_attribute
    def client_id(self) -> str:
        """
        Retrieves the id of the client.
        :return: Such id.
        :rtype: str
        """
        return self._client_id

    @property
    @primary_key_attribute
    def product_id(self):
        """
        Retrieves the id of the product.
        :return: Such id.
        :rtype: str
        """
        return self._product_id

    @property
    @attribute
    def duration(self) -> int:
        """
        Retrieves the duration.
        :return: Such value.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, newValue: int):
        """
        Specifies a new duration.
        :param newValue: The new duration of the order.
        :type newValue: int
        """
        self._duration = newValue

    @property
    @attribute
    def order_date(self):
        """
        Retrieves the order date.
        :return: Such information.
        :rtype: date
        """
        return self._order_date

    @order_date.setter
    def order_date(self, newValue):
        """
        Specifies a new order date.
        :param newValue: The new date.
        :type newValue: date
        """
        self._order_date = newValue
