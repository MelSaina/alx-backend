#!/usr/bin/python3
""" 2-lifo_cache """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class that inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize LIFOCache """
        super().__init__()

    def put(self, key, item):
        """ Assign item to key in self.cache_data """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = list(self.cache_data.keys())[-1]
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        if key is not None:
            return self.cache_data.get(key)
        return None