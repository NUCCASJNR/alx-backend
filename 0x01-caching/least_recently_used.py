#!/usr/bin/env python3

from collections import deque

class LRUCache:
    def __init__(self, capacity):
        """
        capacity: Maximum capacity of queue
        """
        self.capacity = capacity
        self.queue = deque()
        self.cache = {}

    def get(self, key):
        if key in self.cache:
            self.queue.move_to_end(key)
            return self.cache[key]
        return None
    
    def put(self, key, value):
        if key in self.cache:
            # self.queue.move_to_end(key)
            self.cache[key] = value
        else:
            if len(self.cache) >= self.capacity:
                if self.queue:
                    least_used_item = self.queue.popitem(last=False)  # Remove the least recently used item (first item)
                    self.cache.pop(least_used_item[0])  # Remove the corresponding key from the cache
        self.cache[key] = value

        self.cache[key] = value
    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache.keys()):
            print("{}: {}".format(key, self.cache.get(key)))

    def print_queue(self):
        """print queue"""
        print(self.queue)