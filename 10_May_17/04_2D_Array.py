'''
Q1. How do you rotate a matrix by 90° clockwise using Python idioms?
Ans:
Reverse rows, then take transpose: zip(*matrix[::-1]).
'''

# Example
M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Step 0 — show the original matrix
print("Original matrix:", M)
# Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Step 1 — reverse the rows using slicing M[::-1]
rev = M[::-1]
print("After reversing rows:", rev)
# Output: [[7, 8, 9], [4, 5, 6], [1, 2, 3]]

# Step 2 — apply zip(*rev) to transpose the reversed matrix
# zip(*rev) groups elements column-wise
zip_obj = zip(*rev)
print("Zip object:", zip_obj)  # iterator
# Output example: <zip object at ...>

# Convert zip object to list of tuples (to see intermediate result)
zipped_list = list(zip_obj)
print("Zipped (tuples):", zipped_list)
# Output: [(7,4,1), (8,5,2), (9,6,3)]

# Step 3 — convert each tuple to list to get final rotated matrix
rot = [list(row) for row in zipped_list]
print("Rotated matrix (90° clockwise):", rot)
# Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

# Step 4 — one-liner version (compact idiomatic Python)
one_liner = [list(r) for r in zip(*M[::-1])]
print("One-liner result:", one_liner)
# Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]



'''
Q2. When should you switch from lists to NumPy arrays?
Ans:
Switch when you need:
• high performance numeric computing
• vectorized operations
• matrix operations / broadcasting
• working with large datasets (ML, data science)
'''
# Example
import numpy as np
arr = np.array([1,2,3])
print(arr * 10)   # Vectorized: [10,20,30]
