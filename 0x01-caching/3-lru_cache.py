#!/usr/bin/env python3

"""
Contains a LRUCaching class
"""

from base_caching import BaseCaching
from collections import deque, OrderedDict


class LRUCache(BaseCaching):
    """
    LRUcache class that uses the LRU algorithm and inherits from
        Basecaching
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
        self.queue = deque()

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
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = self.queue.popleft()
                self.cache_data.pop(removed)
                print(f"DISCARD: {removed}")
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
            self.queue.append(key)

    def get(self, key):
        """
        Retrieves the value of the key provided from the dict
        Returns none if the key is empty or is not valid key in the dict
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        elif not key or key not in self.cache_data:
            return None
