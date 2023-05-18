#!/usr/bin/python3
""" LRU caching """

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
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
                min = self.get_min(self.key_usage)
                for k, value in self.key_usage.items():
                    if value == min:
                        del self.cache_data[k]
                        print(f"DISCARD: {k}")
                        del self.key_usage[k]
                        break
        self.cache_data[key] = item

    def get_min(self, dico):
        ''' gets the LRU key from a dictionary '''
        return min(dico.values())

    def get(self, key):
        '''gets an item with specified key from cache'''
        if key not in self.cache_data:
            return None

        self.counter += 1
        self.key_usage[key] = self.counter
        return self.cache_data.get(key)
