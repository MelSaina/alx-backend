#!/usr/bin/python3
""" 1-fifo_cache """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class that inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize FIFOCache """
        super().__init__()

    def put(self, key, item):
        """ Assign item to key in self.cache_data """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = next(iter(self.cache_data))
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        if key is not None:
            return self.cache_data.get(key)
        return None