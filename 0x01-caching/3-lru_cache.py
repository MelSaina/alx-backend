#!/usr/bin/python3
""" 3-lru_cache """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class that inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize LRUCache """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Assign item to key in self.cache_data """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.order.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))
            self.cache_data[key] = item
            self.order.append(key)
        else:
            return

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        if key is not None and key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None