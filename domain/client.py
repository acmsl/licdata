from entity import Entity


class Client(Entity):
    """
    Represents a client.
    """

    def __init__(self, id, email, address, contact, phone):
        """Creates a new Client instance"""
        super().__init__(id)
        self._email = email
        self._address = address
        self._contact = contact
        self._phone = phone


    def __str__(self):
        return f"{'id': '{self._id}', 'email': '{self._email}', 'address': '{self._address}', 'contact': '{self._contact}', 'phone': '{self._phone}', 'created': '{self._created}'}"


    @property
    @Entity.primary_key_attribute
    def email(self):
        return self._email


    @property
    @Entity.attribute
    def address(self):
        return self._address


    @property
    @Entity.attribute
    def contact(self):
        return self._contact


    @property
    @Entity.attribute
    def phone(self):
        return self._phone
