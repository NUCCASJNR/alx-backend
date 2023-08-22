#!/usr/bin/env python3

from collections import OrderedDict

class MRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cached = OrderedDict()

    def get(self, key):
        if key in self.cached:
            self.cached.move_to_end(key, last=False)
            return self.cached[key]
        else:
            return None
    
    def put(self, key, value):
        if key in self.cached:
            # Update the value and move the item to the end
            self.cached[key] = value
            self.cached.move_to_end(key)
        else:
            if len(self.cached) >= self.capacity:
                # Cache is full, remove the most recently used item (the last item)
                self.cached.popitem(last=True)
            # Add the new item to the cache and mark it as most recently used
            self.cached[key] = value

    def print_cache(self):
        print(dict(self.cached))