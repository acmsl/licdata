import inspect


class Repo:
    def __init__(self, entityClass):
        self._entityClass = entityClass


    def __str__(self):
        return f"{self._entityClass}"


    @property
    def entityClass(self):
        return self._entityClass


    def findById(self, id):
        """Must be implemented by subclasses"""
        raise NotImplementedError("This method must be implemented by subclasses")


    def findByAttribute(self, attributeName, attributeValue):
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


    def findByPk(self, pk):
        """Must be implemented by subclasses"""
        raise NotImplementedError("This method must be implemented by subclasses")


    def list(self):
        """Must be implemented by subclasses"""
        raise NotImplementedError("This method must be implemented by subclasses")
