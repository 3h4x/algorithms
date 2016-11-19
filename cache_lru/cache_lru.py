class CacheLRU(dict):
    """
        size - cache size
        cache - dict where
            - key is last_used score - higher means more recently used
            - value is our value
    """
    def __init__(self, size):
        if size <= 1:
            raise Exception()
        self.size = size
        self.cache = {}

    def add(self, item):
        if len(self.cache) + 1 > self.size:
            del self.cache[min(self.cache.keys())]

        index = self.recently_used_index()

        self.cache[index] = item

    def recently_used_index(self):
        lru_indexes = self.cache.keys()
        index = 1 if not lru_indexes else max(lru_indexes) + 1
        return index

    def _find_lru_index_of(self, item):
        for index_value, item_value in self.cache.items():
            if item_value == item:
                return index_value

    def get(self, item=None):
        if not item:
            #FIXME: convinient
            return list(self.cache.values())

        if item not in self.cache.values():
            return None

        item_index = self._find_lru_index_of(item)
        if item_index:
            del self.cache[item_index]
            index = self.recently_used_index()
            self.cache[index] = item
            return item

    def pop(self):
        raise NotImplementedError()
