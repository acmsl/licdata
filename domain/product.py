from entity import Entity, primary_key_attribute


class Product(Entity):
    """
    Represents a product.
    """
    def __init__(self, id, product_type_id, product_version):
        """Creates a new Product instance"""
        super().__init__(id)
        self._product_type_id = product_type_id
        self._product_version = product_version


    @property
    @primary_key_attribute
    def product_type_id(self):
        return self._product_type_id


    @property
    @primary_key_attribute
    def product_version(self):
        return self._product_version
