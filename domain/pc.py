from entity import Entity


class Pc(Entity):
    """
    Represents a PC.
    """

    def __init__(self, id, installation_code):
        """Creates a new Pc instance"""
        super().__init__(id)
        self._installation_code = installation_code


    def __str__(self):
        return f"{'id': '{self._id}', 'installation_code': '{self._installation_code}'}"


    @property
    @Entity.primary_key_attribute
    def installation_code(self):
        return self._installation_code
