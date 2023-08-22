#!/usr/bin/env python3

LIFOCache = __import__('lifo_cache').LIFOCache

print(LIFOCache.__qualname__)
print("-----")

lifo_cache = LIFOCache(5)

# Add items to the cache and queue
lifo_cache.put("Name", "Al-Areef")
lifo_cache.put("Age", 16)
lifo_cache.put("Programming_language", "Python|JavaScript")
lifo_cache.put("Hobbies", "Writing codes")
lifo_cache.put("Fun_fact", "I write Backend codes")

print("Printing cache below:")
lifo_cache.print_cache()
print("-----")
print("Printing queue below:")
lifo_cache.print_queue()

print("----")

print("Time to get items from the cache")

print(lifo_cache.get("Name"))
print(lifo_cache.get("Age"))
print(lifo_cache.get("Hobbies"))
print("-----")

print("Time to test our Last in First out attribute")
print("Adding items to the cache and queue even when it has reached its max")

lifo_cache.put("whoami", "root")
print("Printing cache below:")
lifo_cache.print_cache()
print("------")

print("Printing queue below:")
lifo_cache.print_queue()
