'''
1. LRU CACHE
- lru_cache
- It is s a decorator
- It remembers the results of the functions
- So if you call the same function with same arguments again, Python just reuses the stored result instead of running the function again.

2. What does LRU mean exactly?
- LRU = Least Recently Used
- With `maxsize` you can decide how result is cached and stored. 
- The most recently used results are kept.
If the cache gets full, it forgets the oldest used results first. And least recently used one is still there , so that can be used again.
'''

# Example:
from functools import lru_cache

@lru_cache(maxsize=2)
def slow_add(x, y):
    print(f"Calculating {x} + {y}")
    return x + y

slow_add(1, 2)  # Calculated
slow_add(1, 2)  # Cached
slow_add(2, 3)  # Calculated
slow_add(3, 4)  # Calculated → Cache full, oldest dropped
slow_add(1, 2)  # Re-calculated again! ❌ not cached anymore


'''
Some useful functions:
1. func.cache_info() : shows the stats like - "CacheInfo(hits=3, misses=2, maxsize=128, currsize=2)"
2. func.cahe_clear() : empties the cache completely

Catch:
- Does not work well with lists, dict..
'''
