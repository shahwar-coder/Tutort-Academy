'''
Q1. What are the basic built-in data structures in Python?
Ans:
- List → ordered, mutable.
- Tuple → ordered, immutable.
- Set → unordered, unique.
- Dictionary → key-value pairs, mutable.

Example:
'''
lst = [1,2,2,3]      # list allows duplicates
t = (1,2,3)          # tuple immutable
s = {1,2,2,3}        # set keeps only unique values
d = {"a":1,"b":2}    # dict maps keys to values
print(lst, t, s, d)

# Step-by-step:
# List keeps [1,2,2,3]
# Tuple fixed as (1,2,3)
# Set collapses duplicates → {1,2,3}
# Dict stores key-value pairs.




'''
Q2. Why use a tuple instead of a list?
Ans:
- Tuples are immutable → safer for fixed collections.
- Tuples can be used as dict keys, lists cannot.

Example:
'''
coords = (10,20)
location = {coords: "Home"}  # ✅ works
# location[[10,20]] = "Home"  # ❌ error: list is unhashable



'''
Q3. What are sets useful for?
Ans:
- Fast membership checks.
- Removing duplicates.

Example:
'''
nums = [1,2,3,2,1]
unique = set(nums)
print(unique, 2 in unique)

# Step-by-step:
# set(nums) → {1,2,3}
# Membership check 2 in unique → True.



'''
Q4. What does the collections module provide?
Ans:
- Extra data structures:
   - deque → fast appends/pops from both ends.
   - Counter → count frequencies.
   - defaultdict → dict with default values.
   - OrderedDict → dict that remembers insertion order (since Python 3.7, normal dicts do too).
   - namedtuple → lightweight object with fields.

Example:
'''
from collections import Counter, deque
c = Counter("banana")
dq = deque([1,2,3])
dq.appendleft(0)
print(c, dq)

# Step-by-step:
# Counter → {'a':3, 'b':1, 'n':2}
# deque after appendleft → [0,1,2,3]



'''
import heapq
nums = [5,1,3,2]
heapq.heapify(nums)
print(heapq.heappop(nums))

# Step-by-step:
# heapify arranges into heap.
# heappop returns smallest element → 1.
'''
import heapq
nums = [5,1,3,2]
heapq.heapify(nums)
print(heapq.heappop(nums))

# Step-by-step:
# heapify arranges into heap.
# heappop returns smallest element → 1.




'''
Q6. How do external libraries expand data structures?
Ans:
- numpy → efficient arrays.
- pandas → DataFrames for tabular data.
- networkx → graphs.
- Useful for performance and domain-specific tasks.

Example:
'''
import numpy as np
arr = np.array([1,2,3])
print(arr*2)

# Step-by-step:
# numpy array allows vectorized operations.
# [1,2,3]*2 → [2,4,6]



'''
Q7. Why is choosing the right data structure important?
Ans:
- Impacts performance and clarity.
- Example: searching in list = O(n), searching in set/dict = O(1) average.

Example:
'''
lst = [1,2,3,4,5]
s = {1,2,3,4,5}
print(5 in lst, 5 in s)

# Step-by-step:
# In list: scans sequentially (slower).
# In set: hash lookup (faster).



'''
Q8. Quick shorthand
- List = ordered, mutable, duplicates.
- Tuple = ordered, immutable.
- Set = unordered, unique.
- Dict = key-value.
- collections = advanced variants.
- heapq/numpy/pandas = specialized data structures.
'''
