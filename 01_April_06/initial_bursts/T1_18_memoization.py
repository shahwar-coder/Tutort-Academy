'''
1. MEMOIZATION:
- Remember the results of expensive function calls so we don't compute them again.
- Can be thought as a cache that stores results.

2. Why Memoization?
- It saves time in recursive/repeated calculations.
- Avoid duplicate work.
- Turns slow algorithms into fast ones.
'''

# SLOW (without MEMOIZATION) # might not be that slow but for understanding, pretend it is slow (because of repitivie same compute)
def slow_multiply_by_10(n: int)->int:
    """Return num mul by 10"""
    print(f"Calculating for {n}...")
    return n*10

print(slow_multiply_by_10(2))
print(slow_multiply_by_10(2))
print(slow_multiply_by_10(2))

'''
- Calculation once is fine, but agina and again it is done here, just wastage of compute and time.
- Memoization can be a solution to this.
'''

# FAST (with MEMOIZATION)
# Let's MEMOIZE it now!!

from functools import lru_cache

@lru_cache(maxsize=None)
def slow_multiply_by_10(n: int)->int:
    print(f"Calculating for {n}...")
    return n*10

print(slow_multiply_by_10(2))  # ❗ Calculates once
print(slow_multiply_by_10(2))  # ✅ Uses cache
print(slow_multiply_by_10(2))  # ✅ Uses cache
print(slow_multiply_by_10(3))  # ❗ Calculates new
print(slow_multiply_by_10(3))  # ✅ Uses cache
