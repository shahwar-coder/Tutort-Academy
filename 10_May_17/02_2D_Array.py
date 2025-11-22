'''
Q1. What are the time complexities of common list operations?
Ans:
• Index access: O(1)
• Append: O(1) amortized
• Insert/remove at end: O(1) amortized
• Insert/remove in middle: O(n)
• Slicing: O(k) where k is slice size
These matter a lot in algorithmic problems and optimizations.
'''
# Example
nums = [10, 20, 30]
nums.insert(0, 5)  # O(n): shifts elements



'''
Q2. How do you flatten a 2D list (matrix)?
Ans:
Use a nested list comprehension:
[x for row in matrix for x in row]

It extracts each element from every row and places them in a single 1D list.
'''
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

flat = [x for row in matrix for x in row]

print("Original matrix:", matrix)
print("Flattened list:", flat)



'''
Q3. How do you compute the transpose of a 2D list (matrix)?
Ans:
Use zip(*matrix) to group column-wise values together, then convert each group to a list:
[list(col) for col in zip(*matrix)]
'''
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = [list(col) for col in zip(*matrix)]

print("Original matrix:", matrix)
print("Transposed matrix:", transpose)



'''
Q4. Seeing step by step execution, how the transpose happened.
'''

# Step 0 — show the original matrix
print("Original matrix:", matrix)
# Output: Original matrix: [[1, 2, 3], [4, 5, 6]]

# Step 1 — create a zip object using the unpacking operator *
# zip(*matrix) groups the i-th element of each row into a tuple (column-wise)
zip_obj = zip(*matrix)
print("Type of zip object:", type(zip_obj))
# Output: <class 'zip'>

# Convert the zip object into a list to see the grouped tuples
zipped_list = list(zip_obj)
print("zipped_list (tuples):", zipped_list)
# Output: [(1, 4), (2, 5), (3, 6)]

# Step 2 — convert each tuple (column) into a list to form the transposed matrix
transpose = [list(col) for col in zipped_list]
print("Transposed matrix:", transpose)
# Output: [[1, 4], [2, 5], [3, 6]]

# Step 3 — the concise one-liner (equivalent result)
one_liner_transpose = [list(col) for col in zip(*matrix)]
print("One-liner transpose (same result):", one_liner_transpose)
# Output: [[1, 4], [2, 5], [3, 6]]

