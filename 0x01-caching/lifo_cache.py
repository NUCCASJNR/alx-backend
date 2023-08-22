#!/usr/bin/env python3

from collections import deque

class LIFOCache:
    """
    LIFO cache
    """
    def __init__(self, capacity):
        """
        Args:
            capacity: maximum capacity of the cache
        """
        self.capacity = capacity
        self.cache = {}
        self.queue = deque()

    def get(self, key: int | str) -> int | str:
        """
        Returns the value of the key if its present
        and none if its not
        """
        if key in self.cache:
            return self.cache[key]
        return f"{key}: not in {self.cache}"
    
    def put(self, key, value):
        """
        Adds a new key-value pair
        """
        if len(self.cache) >= self.capacity:
            oldest_key = self.queue.pop()
            self.cache.pop(oldest_key)

        self.cache[key] = value
        self.queue.append(key)

    def print_cache(self):
        """print cache"""
        print(self.cache)

    def print_queue(self):
        """print queue"""
        print(self.queue)