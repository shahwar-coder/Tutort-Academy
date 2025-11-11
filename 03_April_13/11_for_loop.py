'''
Q1. How does a for loop work in Python?
Ans:
- Iterates over each element in a sequence (like list, string, range).
- Automatically stops when the sequence ends.
'''
for ch in "hi":
    print(ch)

# Step-by-step:
# First → ch = "h"
# Then → ch = "i"



'''
Q2. What kinds of objects can be used in a for loop?
Ans:
- Any **iterable**: list, tuple, string, dict, set, range, even file objects.
'''
for item in [1, 2, 3]:
    print(item)

# Step-by-step:
# Iterates over list elements one by one.



'''
Q3. How does range() work in for loops?
Ans:
- Produces a sequence of numbers: range(start, stop, step)
- Common in counted loops.
'''
for i in range(1, 6, 2):
    print(i)

# Step-by-step:
# Outputs: 1, 3, 5



'''
Q4. How can you iterate over both index and value?
Ans:
- Use enumerate() for index-value pairs.

Example:
'''
for i, ch in enumerate("abc"):
    print(i, ch)

# Step-by-step:
# i=0, ch="a" → i=1, ch="b" → i=2, ch="c"



'''
Q5. What happens if you loop over a dict?
Ans:
- By default, you get keys.
- You can also loop over .items() or .values().
'''
d = {"a": 1, "b": 2}
for key, val in d.items():
    print(key, val)

# Step-by-step:
# key="a", val=1 → key="b", val=2



'''
Q6. Quick shorthand
- for loops work with any iterable.
- range() for counting.
- enumerate() for index + value.
- dicts → loop over items().
'''
