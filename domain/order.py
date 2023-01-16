from entity import Entity


class Order(Entity):
    """
    Represents an order.
    """

    def __init__(self, id, client_id, product_id, duration, order_date):
        """Creates a new Order instance"""
        super().__init__(id)
        self._client_id = client_id
        self._product_id = product_id
        self._duration = duration
        self._order_date = order_date


    def __str__(self):
        return f"{'id': '{self._id}', 'client_id': '{self._client_id}', 'product_id': '{self._product_id}', 'duration': '{self._duration}', 'order_date': '{self._order_date}', 'created': '{self._created}'}"


    @property
    @Entity.primary_key_attribute
    def client_id(self):
        return self._client_id


    @property
    @Entity.primary_key_attribute
    def product_id(self):
        return self._product_id


    @property
    @Entity.attribute
    def duration(self):
        return self._duration


    @property
    @Entity.attribute
    def order_date(self):
        return self._order_date
