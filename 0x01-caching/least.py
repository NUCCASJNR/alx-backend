#!/usr/bin/env python3

LRUCache = __import__('least_recently_used').LRUCache

least_used =  LRUCache(5)

print(least_used.__dict__)

# Add items to the cache and queue
least_used.put("Name", "Al-Areef")
least_used.put("Age", 16)
least_used.put("Programming_language", "Python|JavaScript")
least_used.put("Hobbies", "Writing codes")
least_used.put("Fun_fact", "I write Backend codes")

print("Printing cache below:")
least_used.print_cache()
print("-----")
print("Printing queue below:")
least_used.print_queue()

print("----")

print("Time to get items from the cache")

print(least_used.get("Name"))
print(least_used.get("Age"))
print(least_used.get("Hobbies"))
print("-----")