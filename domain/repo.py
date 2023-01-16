import inspect


class Repo:
    def __init__(self, entity_class):
        self._entity_class = entity_class


    @property
    def entity_class(self):
        return self._entity_class


    def find_by_id(self, id):
        """Must be implemented by subclasses"""
        raise NotImplementedError("find_by_id() must be implemented by subclasses")


    def find_by_attribute(self, attribute_name, attribute_value):
        """Must be implemented by subclasses"""
        raise NotImplementedError("find_by_attribute() must be implemented by subclasses")


    def filter(self, dictionary):
        """Must be implemented by subclasses"""
        raise NotImplementedError("filter() must be implemented by subclasses")


    def insert(self, item):
        """Must be implemented by subclasses"""
        raise NotImplementedError("insert() must be implemented by subclasses")


    def update(self, item):
        """Must be implemented by subclasses"""
        raise NotImplementedError("update() must be implemented by subclasses")


    def delete(self, id):
        """Must be implemented by subclasses"""
        raise NotImplementedError("delete() must be implemented by subclasses")


    def find_by_pk(self, pk):
        """Must be implemented by subclasses"""
        raise NotImplementedError("find_by_pk() must be implemented by subclasses")


    def list(self):
        """Must be implemented by subclasses"""
        raise NotImplementedError("list() must be implemented by subclasses")
