#!/usr/bin/env python3
from mru import MRUCache

mru_cache = MRUCache(3)
print(mru_cache.__dict__)

mru_cache.put("Name", "Al-Areef")
mru_cache.put("Age", 17)
mru_cache.put("Hobby", "Writing codes")
print(mru_cache.__dict__)
print(mru_cache.get("Name"))

mru_cache.put("language", "Python")
mru_cache.print_cache()