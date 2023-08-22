#!/usr/bin/env python3
FIFOCache = __import__('fifo_cache').FIFOCache

# Create a FIFO cache with a capacity of 3
fifo_cache = FIFOCache(3)

# Add items to the cache
fifo_cache.put("A", 1)
fifo_cache.put("B", 2)
fifo_cache.put("C", 3)
fifo_cache.print_cache()
print("-----")

fifo_cache.print_cache()
print("-----")

fifo_cache.print_queue()
print("------")

# Retrieve items from the cache
print(fifo_cache.get("A"))  # Output: 1
print(fifo_cache.get("B"))  # Output: 2
print(fifo_cache.get("D"))  # Output: None (not in the cache)
fifo_cache.put("D", 4)

print(fifo_cache.get("A"))
print(fifo_cache.get("B"))

