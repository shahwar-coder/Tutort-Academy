'''
Q1. Why do sets automatically remove duplicates in Python?
Ans:
- Sets are **unordered collections of unique elements**.
- When duplicates are added, they’re ignored because of the underlying **hashing mechanism**.
'''
nums = [1, 2, 2, 3, 3, 4]
unique = set(nums)
print(unique)  # {1, 2, 3, 4}



'''
Q2. How do sets achieve uniqueness internally?
Ans:
- Sets use **hash tables**, so each element is hashed.
- If two elements hash to the same value (duplicates), only one is stored.
'''
s = set([10, 10, 20])
print(s)  # {10, 20}
# Internally: second '10' collides on same hash → ignored



'''
Q3. What’s the simplest way to remove duplicates from a list?
Ans:
- Convert it directly to a set, then back to a list.
'''
nums = [4, 2, 2, 1, 3, 3]
print(list(set(nums)))  # [1, 2, 3, 4] (order not guaranteed)



'''
Q4. What if the original order must be preserved?
Ans:
- Use dict.fromkeys(), which preserves insertion order since Python 3.7+.
'''
nums = [1, 2, 2, 3, 3, 1]
unique_ordered = list(dict.fromkeys(nums))
print(unique_ordered)  # [1, 2, 3]



'''
Q5. Why are sets efficient for duplicate removal and comparisons?
Ans:
- Average O(1) insertion and lookup (hash-based).
- Useful for operations like difference, intersection, and union.
'''
a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)  # Intersection → {3}



'''
Q6. Quick shorthand
✔ Sets auto-remove duplicates  
✔ unordered → no index or slicing  
✔ dict.fromkeys() → keep order  
✔ Ideal for uniqueness + fast comparisons  
✔ O(n) performance due to hashing
'''
