#!/usr/bin/python3
""" 4-mru_cache """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class that inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize MRUCache """
        super().__init__()

    def put(self, key, item):
        """ Assign item to key in self.cache_data """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = max(self.cache_data, key=self.cache_data.get)
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))
            self.cache_data[key] = item
        else:
            return

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None