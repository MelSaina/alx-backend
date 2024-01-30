#!/usr/bin/python3
""" 100-lfu_cache """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class that inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize LFUCache """
        super().__init__()
        self.freq_count = {}

    def put(self, key, item):
        """ Assign item to key in self.cache_data """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.freq_count[key] += 1
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    min_freq_keys = [k for k, v in self.freq_count.items() if v == min(self.freq_count.values())]
                    lru_key = min(min_freq_keys, key=lambda x: self.cache_data[x])
                    del self.cache_data[lru_key]
                    del self.freq_count[lru_key]
                    print("DISCARD: {}".format(lru_key))
                self.cache_data[key] = item
                self.freq_count[key] = 1
        else:
            return

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        if key is not None and key in self.cache_data:
            self.freq_count[key] += 1
            return self.cache_data[key]
        return None