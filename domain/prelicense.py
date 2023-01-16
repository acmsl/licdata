from entity import Entity


class Prelicense(Entity):
    """
    Represents a prelicense.
    """

    def __init__(self, id, order_id, seats, duration):
        """Creates a new Prelicense instance"""
        super().__init__(id)
        self._order_id = order_id
        self._seats = seats
        self._duration = duration


    def __str__(self):
        return f"{'id': '{self._id}', 'order_id': '{self._order_id}', 'seats': '{self._seats}', 'duration': '{self._duration}', 'created': '{self._created}'}"


    @property
    @Entity.primary_key_attribute
    def order_id(self):
        return self._order_id


    @property
    @Entity.attribute
    def seats(self):
        return self._seats


    @property
    @Entity.attribute
    def duration(self):
        return self._duration
