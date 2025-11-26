'''
Q1. What is the “Maximum Subarray” problem?
Ans:
It asks for the largest possible sum of a contiguous subarray.
'''
# Example: [−2,1,3,−1,2] → max sum = 5 (1+3+−1+2)

'''
Q2. How does Divide & Conquer approach solve Maximum Subarray?
Ans:
It splits the array into two halves, finds:
1) the best subarray entirely in the LEFT half
2) the best subarray entirely in the RIGHT half
3) the best subarray that CROSSES the middle
Then it returns the maximum of these three values.
'''
# Example: Step-by-step (Divide & Conquer)

# Array = [2, -1, 3, -4, 5]
# Goal = maximum subarray sum

# Step 1: Split the array
#     Left half  = [2, -1, 3]
#     Right half = [-4, 5]

# Step 2: Solve LEFT half recursively
#     Best left subarray = 2 + (-1) + 3 = 4

# Step 3: Solve RIGHT half recursively
#     Best right subarray = 5

# Step 4: Find BEST CROSSING SUBARRAY
#     It must include:
#         - the best sum ending at the last element of LEFT
#         - the best sum starting at the first element of RIGHT

#     From left part:
#         [2, -1, 3] → best ending at last element = 2 + (-1) + 3 = 4

#     From right part:
#         [-4, 5] → best starting at first element = max(-4, -4+5=1, 5) = 5

#     Crossing sum = 4 (left end) + 5 (right start) = 9

# Step 5: Compare all three
#     left_best     = 4
#     right_best    = 5
#     crossing_best = 9

# Answer = max(4, 5, 9) = 9


# # Divide:
#     Split into left half and right half.

# # Conquer:
#     Recursively find best subarray in each half.

# # Combine:
#     Compute crossing sum and take the maximum of the three results.


'''
Q3. What is the “crossing subarray” in this algorithm?
Ans:
It is the maximum subarray that starts in the left half and ends in the right half.
'''
# Example: left prefix ending at mid + right prefix starting mid+1.



'''
Q4. Why do we take the max of (left, right, crossing)?
Ans:
Because the best subarray could be fully left, fully right, or spread across both halves.
'''
# Example:
# If left gives 10, right gives 12, crossing gives 15 → answer = 15.


'''
Q5. What is the time complexity of this Divide & Conquer solution?
Ans:
O(n log n) because each level does O(n) work and there are log n levels.
'''
# Example: classic merge-sort-style splitting.


'''
Q6. Why is Kadane’s Algorithm faster?
Ans:
Kadane does the same job in O(n) by iterating once, without splitting.
'''
# Example:
# Running sum resets on negative → track global maximum.

