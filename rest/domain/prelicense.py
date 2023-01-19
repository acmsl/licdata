from entity import Entity, primary_key_attribute, attribute


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


    @property
    @primary_key_attribute
    def order_id(self):
        return self._order_id


    @property
    @attribute
    def seats(self):
        return self._seats


    @seats.setter
    def seats(self, newValue):
        self._seats = newValue


    @property
    @attribute
    def duration(self):
        return self._duration


    @duration.setter
    def duration(self, newValue):
        self._duration = newValue
