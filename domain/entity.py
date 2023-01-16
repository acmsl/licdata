from datetime import datetime


class Entity():

    __primary_key_attributes = []
    __filter_attributes = []
    __attributes = []

    @classmethod
    def primary_key_attribute(cls, func):
        cls.__primary_key_attributes.append(func.__name__)
        cls.__attributes.append(func.__name__)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)


    @classmethod
    def filter_attribute(cls, func):
        cls.__filter_key_attributes.append(func.__name__)
        cls.__attributes.append(func.__name__)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)


    @classmethod
    def attribute(cls, func):
        cls.__attributes.append(func.__name__)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)


    @classmethod
    def primary_key(cls):
        return cls.__primary_key_attributes


    @classmethod
    def filter_attributes(cls):
        return cls.__filter_attributes


    @classmethod
    def attributes(cls):
        return cls.__attributes


    """
    Represents an entity.
    """
    def __init__(self, id):
        """Creates a new Entity instance"""
        self._id = id
        self._created = datetime.now()


    @property
    def id(self):
        return self._id


    @property
    @attribute
    def created(self):
        return self._created
