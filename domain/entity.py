import functools
from datetime import datetime
import inspect
import re

_primary_key_attributes = {}
_filter_attributes = {}
_attributes = {}

def attribute(func):
    key = inspect.getmodule(func).__name__
    if not key in _attributes:
        _attributes[key] = [ ]
    _attributes[key].append(func.__name__)
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)


def primary_key_attribute(func):
    key = inspect.getmodule(func).__name__
    if not key in _primary_key_attributes:
        _primary_key_attributes[key] = []
    _primary_key_attributes[key].append(func.__name__)
    attribute(func)
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)


def filter_attribute(func):
    key = inspect.getmodule(func).__name__
    if not key in _filter_attributes:
        _filter_attributes[key] = []
    _filter_attributes[key].append(func.__name__)
    attribute(func)
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)


class Entity:

    @classmethod
    def primary_key(cls):
        result = []
        key = cls.__module__
        if key in _primary_key_attributes:
            result = _primary_key_attributes[key]
        return result


    @classmethod
    def filter_attributes(cls):
        result = []
        key = cls.__module__
        if key in _filter_attributes:
            result = _filter_attributes[key]
        return result


    @classmethod
    def attributes(cls):
        result = []
        key = cls.__module__
        if key in _attributes:
            result = _attributes[key]
        return [ "id" ] + result + [ "created" ]


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
    def created(self):
        return self._created


    def __str__(self):
        result = []
        if self.__class__.__name__ in _attributes:
            result.append(f"'id': '{self._id}'")
            for attr in _attributes[self.__class__.__name__]:
                result.append(f"'{attr}': '" + str(getattr(self, f"_{attr}")) + "'")
        return "{ " + ", ".join(result) + " }"
