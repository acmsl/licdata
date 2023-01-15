import inspect


class Entity():

    __primaryKeyAttributes = []
    __filterAttributes = []
    __attributes = []

    """
    Represents an entity.
    """
    def __init__(self):
        """Creates a new Entity instance"""
        pass


    @classmethod
    def primaryKeyAttribute(cls, func):
        cls.__primaryKeyAttributes.append(func.__name__)
        cls.__attributes.append(func.__name__)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)


    @classmethod
    def filterAttribute(cls, func):
        cls.__filterKeyAttributes.append(func.__name__)
        cls.__attributes.append(func.__name__)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)


    @classmethod
    def attribute(cls, func):
        cls.__attributes.append(func.__name__)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)



    @classmethod
    def primaryKey(cls):
        return cls.__primaryKeyAttributes


    @classmethod
    def filterAttributes(cls):
        return cls.__filterAttributes


    @classmethod
    def attributes(cls):
        return cls.__attributes
