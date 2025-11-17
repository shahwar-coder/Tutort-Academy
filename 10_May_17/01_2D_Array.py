'''
Q1. What is the difference between Python lists, array.array, and NumPy arrays?
Ans:
• List → flexible, can hold mixed types, most commonly used.
• array.array → typed, compact storage, only holds one data type, limited operations.
• NumPy ndarray → fixed-type, extremely fast, supports vectorized computation, used for scientific/numeric work.
Use lists for general coding, NumPy for performance-heavy numeric tasks.
'''
# Example
from array import array
import numpy as np

lst = [1, 2, 3]
arr = array('i', [1, 2, 3])
npa = np.array([1, 2, 3])

print(lst, arr, npa)



'''
Q2. How do you correctly create a 2D list (matrix) without shared references?

Ans:
In Python, using [[0]*cols]*rows is incorrect because it creates multiple
rows that all point to the SAME inner list. Changing one row changes all.

Correct way:
Use list comprehension → [[0]*cols for _ in range(rows)]
This creates a NEW independent list for every row.

Key idea:
• Wrong: rows share the same memory
• Right: each row has its own memory
'''
rows, cols = 3, 3

# Correct (independent rows)
good = [[0]*cols for _ in range(rows)]

# Incorrect (shared rows)
bad = [[0]*cols]*rows

good[1][1] = 7
bad[1][1] = 7

print("GOOD MATRIX (only one change):")
for r in good:
    print(r)

# [0, 0, 0]
# [0, 7, 0]   ← only this row changed
# [0, 0, 0]

print("\nBAD MATRIX (all rows changed):")
for r in bad:
    print(r)

# [0, 7, 0]
# [0, 7, 0]   ← same change appears everywhere! ❗ changed automatically
# [0, 7, 0]   ❗ changed automatically



'''
Q3. Visual Explanation for BAD version vs GOOD version:
'''
# BAD version (shared references):
#     [[0,0,0,0],
#      [0,0,0,0],
#      [0,0,0,0]]

# Internally → all rows point to the SAME list:
#     row1 ─┐
#     row2 ─┼──► [0,0,0,0]
#     row3 ─┘

# If you change bad[0][0] = 99, the single shared row updates:
#     [[99,0,0,0],
#      [99,0,0,0],
#      [99,0,0,0]]

# ===========================================

# GOOD version (independent rows):
#     [[0,0,0,0],
#      [0,0,0,0],
#      [0,0,0,0]]

# Internally → each row is a new list:
#     row1 ─► [0,0,0,0]
#     row2 ─► [0,0,0,0]
#     row3 ─► [0,0,0,0]

# If you change good[0][0] = 99:
#     [[99,0,0,0],
#      [0,0,0,0],
#      [0,0,0,0]]

# Only the first row changes — perfect!
