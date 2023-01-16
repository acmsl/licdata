from entity import Entity


class ProductType(Entity):
    """
    Represents a product type.
    """

    def __init__(self, id, name, version):
        """Creates a new ProductType instance"""
        super().__init__(id)
        self._name = name
        self._version = version


    def __str__(self):
        return f"{'id': '{self._id}', 'name': '{self._name}', 'version': '{self._version}', 'created': '{self._created}'}"


    @property
    @Entity.primary_key_attribute
    def name(self):
        return self._name


    @property
    @Entity.primary_key_attribute
    def version(self):
        return self._version
