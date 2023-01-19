from entity import Entity, primary_key_attribute


class Incident(Entity):
    """
    Represents a incident.
    """

    def __init__(self, id, license_id, pc_id):
        """Creates a new Incident instance"""
        super().__init__(id)
        self._license_id = license_id
        self._pc_id = pc_id


    @property
    @primary_key_attribute
    def license_id(self):
        return self._license_id


    @property
    @primary_key_attribute
    def pc_id(self):
        return self._pc_id
