import github_adapter

class GithubRepo():
    def __init__(self, path, primary_key, filter_attributes, attributes):
        self._path = path
        self._primary_key = primary_key
        self._filter_attributes = filter_attributes
        self._attributes = attributes


    def __str__(self):
        return f"path: {self._path} pk: {self._primary_key}, filters: {self._filter_attributes}, attributes: {self._attributes}"


    @property
    def path(self):
        return self._path


    @property
    def primary_key(self):
        return self._primary_key


    @property
    def filter_attributes(self):
        return self._filter_attributes


    @property
    def attributes(self):
        return self._attributes


    def find_by_id(self, id):
        return github_adapter.find_by_id(id, self._path)


    def find_by_attribute(self, attribute_name, attribute_value):
        return github_adapter.find_by_attribute(attribute_value, attribute_name, self._path)


    def find_by_attributes(self, filter):
        return github_adapter.find_by_attributes(filter, self._path)


    def insert(self, item):
        return github_adapter.insert(item, self._path, self._primary_key, self._filter_attributes, self._attributes)


    def update(self, item):
        return github_adapter.update(
            item, self._path, self._primary_key, self._filter_attributes, self._attributes)


    def delete(self, id):
        return github_adapter.delete(id, self._path)


    def find_by_pk(self, pk):
        return github_adapter.find_by_attributes(pk, self._path)


    def list(self):
        return github_adapter.list(self._path)
