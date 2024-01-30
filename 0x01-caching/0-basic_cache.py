#!/usr/bin/python3
""" 0-basic_cache """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ 
    BasicCache class that inherits from BaseCaching
    
    """

    def put(self, key, item):
        """ 
        Assign item to key in self.cache_data 
        
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ 
        Return the value in self.cache_data linked to key 
        
        """
        if key is not None:
            return self.cache_data.get(key)
        return None