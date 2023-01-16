import inspect


class Repo:
    def __init__(self, entityClass):
        self._entityClass = entityClass


    def __str__(self):
        return f"{self._entityClass}"


    @property
    def entity_class(self):
        return self._entityClass


    def find_by_id(self, id):
        """Must be implemented by subclasses"""
        raise NotImplementedError("This method must be implemented by subclasses")


    def find_by_attribute(self, attributeName, attributeValue):
        """Must be implemented by subclasses"""
        raise NotImplementedError("This method must be implemented by subclasses")


    def filter(self, dictionary):
        """Must be implemented by subclasses"""
        raise NotImplementedError("This method must be implemented by subclasses")


    def insert(self, item):
        """Must be implemented by subclasses"""
        raise NotImplementedError("This method must be implemented by subclasses")


    def update(self, item):
        """Must be implemented by subclasses"""
        raise NotImplementedError("This method must be implemented by subclasses")


    def delete(self, id):
        """Must be implemented by subclasses"""
        raise NotImplementedError("This method must be implemented by subclasses")


    def find_by_pk(self, pk):
        """Must be implemented by subclasses"""
        raise NotImplementedError("This method must be implemented by subclasses")


    def list(self):
        """Must be implemented by subclasses"""
        raise NotImplementedError("This method must be implemented by subclasses")
