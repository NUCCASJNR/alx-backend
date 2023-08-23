#!/usr/bin/env python3

"""
Contains a LRUCaching class
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    LRUcache class that uses the LRU algorithm and inherits from
        Basecaching
    """
    def __init__(self):
        super().__init__()
        self.data = OrderedDict()

    def put(self, key, item):
        """
        Adds a new key-value pair to the cache
        Args:
            Key: Key to be added
            item: Value of the added key
        """
        if key is None or item is None:
            pass
        if key in self.cache_data:
            self.cache_data[key] = item
            self.data[key] = item
            self.data.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Get the first key from the ordered dict
                removed = next(iter(self.data))
                print(f"DISCARD: {removed}")
                # pop it out from both the ordered dict and the usual dict
                self.cache_data.pop(removed)
                self.data.pop(removed)
            # Add the key-value pair to the two dicts
            self.cache_data[key] = item
            self.data[key] = item
            self.data.move_to_end(key)

    def get(self, key):
        """
        Retrieves the value of the key provided from the dict
        Returns none if the key is empty or is not valid key in the dict
        """
        if key in self.data:
            self.data.move_to_end(key)
            return self.cache_data[key]
        elif not key or key not in self.cache_data:
            return None
