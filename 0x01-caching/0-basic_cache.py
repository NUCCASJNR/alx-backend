#!/usr/bin/env python3
"""
contains a cache class
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A basiccache class that inherits from the BaseCaching class
    """
    def put(self, key, item):
        """
        Adds a new key-value pair to the cache
        Args:
            Key: Key to be added
            item: Value of the added key
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the value of the key provided from the dict
        Returns none if the key is empty or is not valid key in the dict
        """
        if key in self.cache_data:
            return self.cache_data[key]
        elif not key or key not in self.cache_data:
            return None
