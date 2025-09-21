'''
🔹 Python `tuple` Type

- A `tuple` is an **ordered**, **immutable** sequence in Python.
- Tuples are like lists, but **cannot be modified** once created.
- Ideal for storing **fixed collections** of items or as **dictionary keys** (hashable).

🔸 Tuple Creation:
    t1 = (1, 2, 3)
    t2 = "a", "b", "c"         # parentheses optional
    t3 = ()                    # empty tuple
    t4 = (5,)                  # single-element tuple must have comma
    t5 = tuple([1, 2, 3])      # from list

🔸 Accessing Elements:
    t1[0]          → First element
    t1[-1]         → Last element
    t1[1:3]        → Slice (elements at index 1 and 2)

🔸 Immutability:
- Cannot add, remove, or modify items.
- But if it contains mutable elements (like a list), those can be changed:
    t = ([1, 2], 3)
    t[0][0] = 99   → Valid because the list is mutable

🔸 Useful Methods:
- `.count(x)`     → Number of times `x` occurs
- `.index(x)`     → First index of `x`

🔸 Advantages over Lists:
- **Faster** due to immutability
- **Hashable**: usable as keys in dictionaries or elements in sets
- **Safer** for write-protected data

🔸 Tuple Unpacking:
    a, b = (10, 20)           → a = 10, b = 20
    x, y, z = (1, 2, 3)

🔸 Packing and Unpacking:
    packed = 1, 2, 3          # packing
    a, b, c = packed          # unpacking

🔸 Nesting:
    t = ((1, 2), (3, 4))
    t[1][0] → 3

🔸 Iteration:
    for item in t1:
        print(item)

🔸 Membership:
    2 in t1         → True
    5 not in t1     → True

🔸 When to Use:
- Use `tuple` when:
    ✅ You want a fixed, unchangeable sequence.
    ✅ You want to ensure data integrity.
    ✅ You need it as a key in a dictionary or element in a set.
'''

point = (4, 5)
x, y = point
print(f"x = {x}, y = {y}")   # x = 4, y = 5
