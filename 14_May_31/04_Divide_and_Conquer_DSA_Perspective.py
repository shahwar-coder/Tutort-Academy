'''
Q1. Why does Binary Search use Divide & Conquer?
Ans:
Because it divides the array into halves again and again until the target is found.
'''
# Example: Binary Search (Step-by-Step)

# Array = [2, 5, 8, 12, 16, 23, 38]
# Target = 16

# Step 1:
#     left = 0
#     right = 6
#     mid = (0 + 6) // 2 = 3
#     array[mid] = 12

#     Since 12 < 16 → search the RIGHT half.

# Step 2:
#     left = 4
#     right = 6
#     mid = (4 + 6) // 2 = 5
#     array[mid] = 23

#     Since 23 > 16 → search the LEFT half of this region.

# Step 3:
#     left = 4
#     right = 4
#     mid = (4 + 4) // 2 = 4
#     array[mid] = 16

#     Found the target!

# # Divide:
#     Split array into halves at mid.

# # Conquer:
#     Choose either left half or right half.

# # Combine:
#     Return the result (no merging needed).



'''
Q2. What does the “Conquer” step mean in Binary Search?
Ans:
Solving the smaller chosen half by repeating the same procedure.
'''
# Example: Recalculate mid inside the smaller half.

