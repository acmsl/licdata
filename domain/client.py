from entity import Entity, primary_key_attribute, attribute


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


    @property
    @primary_key_attribute
    def email(self):
        return self._email


    @property
    @attribute
    def address(self):
        return self._address


    @property
    @attribute
    def contact(self):
        return self._contact


    @property
    @attribute
    def phone(self):
        return self._phone
