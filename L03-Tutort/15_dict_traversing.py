'''
Q1. How do you loop through a dictionary in Python?
Ans:
- Use `.items()` to get both key and value during iteration.
'''
d = {"a": 1, "b": 2}
for key, val in d.items():
    print(key, val)

# Step-by-step:
# First: key="a", val=1
# Then: key="b", val=2



'''
Q2. What does .items() return?
Ans:
- Returns a view of (key, value) pairs as tuples.
- Iterable → can be used in for-loops, list comps, etc.
'''
print(list(d.items()))
# Output: [('a', 1), ('b', 2)]



'''
Q3. What happens if you loop without .items()?
Ans:
- You only get the keys.
- Values require a second lookup (less efficient).
'''
for key in d:
    print(key, d[key])  # works, but extra lookup

# Preferred: for key, val in d.items()



'''
Q4. How can you filter a dictionary while looping?
Ans:
- Use a conditional inside the loop.

Example:
'''
for k, v in d.items():
    if v % 2 == 0:
        print(f"{k} → even value")

# Step-by-step:
# Checks each value, prints if even.



'''
Q5. Can you transform keys or values while looping?
Ans:
- Yes, use dictionary comprehensions or build a new dict.

Example:
'''
d = {"a": 1, "b": 2}
squared = {k: v**2 for k, v in d.items()}
print(squared)  # {'a': 1, 'b': 4}



'''
Q6. Quick shorthand
- d.items() → (key, value) pairs
- d.keys(), d.values() → just keys or just values
- Prefer .items() for full access
'''
