'''
Q1. What is dict mapping (also called dispatch table)?
Ans:
- It maps keys to values or actions (functions).
- A powerful alternative to if-elif chains when branching on a known key.
'''
def greet(): return "Hello"
def bye(): return "Goodbye"

actions = {"hi": greet, "bye": bye}
print(actions["hi"]())  # → "Hello"

# Step-by-step:
# 1. Lookup key "hi" → gets greet.
# 2. Call the function → returns "Hello".

# Example 2:
actions = {1: "One", 2: "Two", 3: "Three"}
print(actions.get(2, "Other"))

# Step-by-step:
# Lookup key=2 → "Two".




'''
Q2. How do you handle default/fallback with dict mapping?
Ans:
- Use `.get(key, default)` to avoid KeyError.

Example:
'''
color_map = {
    'r': 'Red',
    'g': 'Green',
    'b': 'Blue'
}

code = 'y'  # not in the dictionary
color = color_map.get(code, 'Unknown')

print(color)  # Output: Unknown



'''
Q3 (same as Q2). How do you provide a default safely?
Ans:
- Use dict.get(key, default).
- Prevents KeyError for missing keys.
'''
actions = {1: "One", 2: "Two"}
print(actions.get(3, "Other"))

# Step-by-step:
# Key=3 not in dict.
# .get returns default "Other".



'''
Q3. How can functions be stored in dicts?
Ans:
- Store function objects as values.
- Call them after lookup.
'''
def greet(): return "Hello"
def bye(): return "Goodbye"

dispatch = {"hi": greet, "bye": bye}
print(dispatch["hi"]())

# Step-by-step:
# Key="hi" → greet function.
# Call it → "Hello".



'''
Q4. How can you pre-configure functions in a dict?
Ans:
- Use functools.partial or lambdas.
- Helpful when functions need arguments.

Example:
'''
from functools import partial

def power(base, exp): return base**exp
dispatch = {"square": partial(power, exp=2)}

print(dispatch )

# Step-by-step:
# partial locks exp=2.
# power(5,2) → 25.



'''
Q5. When should you use dict mapping vs match-case?
Ans:
- Dict mapping: good for key → action lookups.
- match-case: better for structural pattern matching (tuples, complex conditions).
'''



'''
Q6. Quick shorthand
- Dict mapping = key → value/function.
- Use .get for defaults.
- Store functions for dynamic actions.
- Pre-configure with partial/lambda.
- Cleaner than long if-elif for key-based routing.
'''

