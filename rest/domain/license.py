from entity import Entity, primary_key_attribute, attribute


class License(Entity):
    """
    Represents a license.
    """
    def __init__(self, id, client_id, product_id, duration, order_date):
        """Creates a new License instance"""
        super().__init__(id)
        self._client_id = client_id
        self._product_id = product_id
        self._duration = duration
        self._order_date = order_date


    @property
    @primary_key_attribute
    def client_id(self):
        return self._client_id


    @property
    @primary_key_attribute
    def product_id(self):
        return self._product_id


    @property
    @attribute
    def duration(self):
        return self._duration


    @duration.setter
    def duration(self, newValue):
        self._duration = newValue


    @property
    @attribute
    def order_date(self):
        return self._order_date


    @order_date.setter
    def order_date(self, newValue):
        self._order_date = newValue
