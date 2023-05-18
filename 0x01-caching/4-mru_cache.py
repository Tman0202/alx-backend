#!/usr/bin/python3
""" MRU caching """

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    ''' Least Recently Used Caching System '''
    def __init__(self):
        self.key_usage = {}
        self.counter = 0
        self.cache_data = {}
        super().__init__()

    def put(self, key, item):
        ''' Adds an item to the cache
            Removes last item if cache size is
            greater than BaseCaching.MAX_ITEMS
        '''
        if key is None or item is None:
            return

        if self.counter < 1:
            self.key_usage[key] = self.counter
        else:
            self.counter += 1
            self.key_usage[key] = self.counter
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data:
                mru = self.get_mru(self.key_usage) - 1
                for k, value in self.key_usage.items():
                    if value == mru:
                        del self.cache_data[k]
                        print(f"DISCARD: {k}")
                        del self.key_usage[k]
                        break
        self.cache_data[key] = item

    def get_mru(self, dico):
        ''' gets the MRU key from a dictionary '''
        return max(dico.values())

    def get(self, key):
        '''gets an item with specified key from cache'''
        if key not in self.cache_data:
            return None

        self.counter += 1
        self.key_usage[key] = self.counter
        return self.cache_data.get(key)
