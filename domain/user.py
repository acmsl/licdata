from entity import Entity, primary_key_attribute


class User(Entity):
    """
    Represents a user.
    """
    def __init__(self, id, email, password):
        """Creates a new User instance"""
        super().__init__(id)
        self._email = email
        self._password = password


    @property
    @filter_attribute
    def email(self):
        return self._email


    @email.setter
    def email(self, newValue):
        self._email = newValue


    @property
    @filter_attribute
    def password(self):
        return self._password


    @password.setter
    def password(self, newValue):
        self._password = newValue
