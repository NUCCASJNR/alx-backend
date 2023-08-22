#!/usr/bin/env python3

from collections import deque

class FIFOCache:
    def __init__(self, capacity):
        self.capacity = capacity  # Maximum number of items the cache can hold
        self.cache = {}  # Dictionary to store cached items
        self.queue = deque()  # Queue to keep track of the order of items

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        else:
            return f"{key}: not in {self.cache}" # Return None if the item is not in the cache

    def put(self, key, value):
        if len(self.cache) >= self.capacity:
            # Cache is full, remove the oldest item
            oldest_key = self.queue.popleft()
            self.cache.pop(oldest_key)
        
        # Add the new item to the cache and the queue
        self.cache[key] = value
        # self.queue.append(key)

    def print_cache(self):
        """print cache"""
        print(self.cache)

    def print_queue(self):
        """print queue"""
        print(self.queue)