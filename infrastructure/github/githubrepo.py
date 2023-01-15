import githubadapter

class GithubRepo():
    def __init__(self, path, primaryKey, filterAttributes, attributes):
        self._path = path
        self._primaryKey = primaryKey
        self._filterAttributes = filterAttributes
        self._attributes = attributes


    def __str__(self):
        return f"path: {self._path} pk: {self._primaryKey}, filters: {self._filterAttributes}, attributes: {self._attributes}"


    @property
    def path(self):
        return self._path


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
        return githubadapter.findById(id, self._path)


    def findByAttribute(self, attributeName, attributeValue):
        return githubadapter.findByAttribute(attributeValue, attributeName, self._path)


    def insert(self, item):
        return githubadapter.insert(item, self._path, self._filterAttributes, self._attributes)


    def update(self, item):
        return githubadapter.update(
            item, self._path, self._filterAttributes, self._attributes)


    def delete(self, id):
        return githubadapter.delete(id, self._path)


    def findByPk(self, pk):
        print(pk)
        filter = {}
        for idx, attr in enumerate(self._primaryKey):
            filter[attr] = pk[idx]

        return githubadapter.findByAttributes(filter, self._path)


    def list(self):
        return githubadapter.list(self._path)
