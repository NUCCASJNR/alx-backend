#!/usr/bin/env python3

"""
Contains a FifoCache class
"""

from base_caching import BaseCaching
from collections import deque


class FIFOCache(BaseCaching):
    """
    FifoCache classs that inherits from basecaching
    """
    def __init__(self):
        super().__init__()
        self.queue = deque()
        self.cache_data = {}

    def put(self, key, item):
        """
        Adds a new key-value pair to the cache
        Args:
            Key: Key to be added
            item: Value of the added key
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    self.cache_data[key] = item
                else:
                    removed_item = self.queue.popleft()
                    self.cache_data.pop(removed_item)
                    print(f"DISCARD: {removed_item}")
            self.cache_data[key] = item
            self.queue.append(key)
            print(self.queue)

    def get(self, key):
        """
        Retrieves the value of the key provided from the dict
        Returns none if the key is empty or is not valid key in the dict
        """
        if key in self.cache_data:
            return self.cache_data[key]
        elif not key or key not in self.cache_data:
            return None
