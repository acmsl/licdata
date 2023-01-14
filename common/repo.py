import githubrepo

class Repo:
    def __init__(self, entityType, primaryKey, filterAttributes, attributes):
        self._entityType = entityType
        self._primaryKey = primaryKey
        self._filterAttributes = filterAttributes
        self._attributes = attributes

    def __str__(self):
        return f"{self._entityType} pk: {self._primaryKey}, filters: {self._filterAttributes}, attributes: {self._attributes}"

    @property
    def entityType(self):
        return self._entityType


    @property
    def primaryKey(self):
        return self._primaryKey


    @property
    def filterAttributes(self):
        return self._filterAttributes


    @property
    def attributes(self):
        return self._attributes


    def findById(self, id):
        return githubrepo.findById(id, self._entityType)


    def findByAttribute(self, attributeName, attributeValue):
        return githubrepo.findByAttribute(attributeValue, attributeName, self._entityType)


    def insert(self, item):
        return githubrepo.insert(item, self._entityType, self._filterAttributes, self._attributes)


    def update(self, item):
        return githubrepo.update(
            item, self._entityType, self._filterAttributes, self._attributes)


    def delete(self, id):
        return githubrepo.delete(id, self._entityType)


    def findByPk(self, pk):
        print(pk)
        filter = {}
        for idx, attr in enumerate(self._primaryKey):
            filter[attr] = pk[idx]

        return githubrepo.findByAttributes(filter, self._entityType)


    def list(self):
        return githubrepo.list(self._entityType)
