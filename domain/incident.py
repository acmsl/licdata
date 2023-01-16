from entity import Entity


class Incident(Entity):
    """
    Represents a incident.
    """

    def __init__(self, id, license_id, pc_id):
        """Creates a new Incident instance"""
        super().__init__(id)
        self._license_id = license_id
        self._pc_id = pc_id

    def __str__(self):
        return f"{'id': '{self._id}', 'order_id': '{self._order_id}', 'license_id': '{self._license_id}', 'pc_id': '{self._pc_id}', 'created': '{self._created}'}"


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
