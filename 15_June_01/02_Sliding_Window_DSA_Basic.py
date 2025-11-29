'''
Q1. What is the basic formula for updating a fixed-size window?
Ans:
new_sum = old_sum - arr[left] + arr[right]
'''

# Example (step-by-step):

# Consider the array:
# arr = [2, 1, 3, 2, 4]

# Let the window size = 3.

# --- Initial window (positions and values) ---
# Window covers indices [0, 1, 2]:
#   values = [2, 1, 3]
#   left  = 0   (points at value 2)
#   right = 2   (points at value 3)

# Compute the initial sum explicitly (digit-by-digit):
#   old_sum = 2 + 1 + 3
#           = 3 + 3       (compute 2 + 1 = 3, then + 3)
#           = 6

# So: Window [2, 1, 3] → sum = 6

# --- Slide the window one step to the right ---
# New window should cover indices [1, 2, 3]:
#   values = [1, 3, 2]
#   new_left  = 1   (value leaving the window: arr[left] = arr[0] = 2)
#   new_right = 3   (value entering the window: arr[3] = 2)

# Apply the formula:
#   new_sum = old_sum - arr[left] + arr[right]
#           = 6 - arr[0] + arr[3]
#           = 6 - 2 + 2

# Compute carefully, left-to-right:
#   6 - 2 = 4
#   4 + 2 = 6

# So the updated sum is 6 — the window [1, 3, 2] also sums to 6.

# Verify by direct addition (sanity check):
#   1 + 3 + 2 = 4 + 2 = 6  ✅

# Move the left/right pointers for the next slide:
#   left  becomes 1
#   right becomes 3
#   old_sum for the next step = 6

# --- Slide the window one more step to the right ---
# New window indices [2, 3, 4]:
#   values = [3, 2, 4]
#   leaving value = arr[1] = 1
#   entering value = arr[4] = 4

# Use formula:
#   new_sum = old_sum - arr[left] + arr[right]
#           = 6 - 1 + 4

# Compute step-by-step:
#   6 - 1 = 5
#   5 + 4 = 9

# So the sum for window [3, 2, 4] = 9.

# Verify directly:
#   3 + 2 + 4 = 5 + 4 = 9  

# --- Summary (what changed each slide) ---
# 1. Start: window [2,1,3] → sum = 6
# 2. Slide 1: removed 2, added 2 → 6 - 2 + 2 = 6 → window [1,3,2]
# 3. Slide 2: removed 1, added 4 → 6 - 1 + 4 = 9 → window [3,2,4]

# Key idea: instead of recomputing the sum of all k elements, subtract the element that falls out and add the new entering element — that gives O(1) update per slide.



'''
Q2. How do you compute the first window sum of size k?
Ans:
Add the first k elements using a simple loop.
'''
# Example:
# k=3 → sum = arr[0] + arr[1] + arr[2]



'''
Q3. When sliding a fixed window by one step, what happens to left and right pointers?
Ans:
left moves one step right, and right also moves one step right.
'''
# Example:
# left:0→1, right:2→3



'''
Q4. What is the common loop structure for fixed-window problems?
Ans:
Build the first window, then from i=k to n-1 update the window by:
   subtracting arr[i-k],
   adding arr[i].
'''
# Example:
# For i in range(k, n):
#   sum += arr[i] - arr[i-k]
# ============================
# Example Explanation:

# arr = [4, 2, 1, 7, 3]
# k = 3

# STEP 1 — Build the first window:
# Window = [4, 2, 1]
# Sum = 4 + 2 + 1 = 7

# We now slide the window using:
# for i in range(k, n):

# ------------------------------
# Iteration 1 → i = 3
# New element entering  = arr[3] = 7
# Element leaving       = arr[0] = 4

# Apply formula:
# window_sum = 7 + 7 - 4 = 10

# New window = [2, 1, 7]
# New sum    = 10
# ------------------------------

# Iteration 2 → i = 4
# New element entering  = arr[4] = 3
# Element leaving       = arr[1] = 2

# Apply formula:
# window_sum = 10 + 3 - 2 = 11

# New window = [1, 7, 3]
# New sum    = 11
# ------------------------------

# Final Summary:
# Start:    [4,2,1] → 7
# Slide #1: [2,1,7] → 10
# Slide #2: [1,7,3] → 11



'''
Q5. How does a variable window usually expand?
Ans:
Right pointer moves forward and adds arr[right] to the current sum or condition state.
'''
# Example:
# right++ while sum < target



'''
Q6. When does a variable window shrink?
Ans:
Shrink from the left while the condition is satisfied (like sum >= target).
'''
# Example:
# while sum >= target: sum -= arr[left]; left++



'''
Q7. What are the two pointers used in sliding window?
Ans:
left (start of window) and right (end of window).
They define the current active window.
'''
# Example:
# Window = arr[left:right+1]
