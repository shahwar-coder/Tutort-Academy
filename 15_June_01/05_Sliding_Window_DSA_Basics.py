'''
Q1. What triggers window expansion in a variable sliding window?
Ans:
The right pointer moves right and we update the window condition.
'''
# Example: window_sum += arr[right]

'''

Q2. What triggers window shrinkage?
Ans:
Shrink while the window violates the rule (e.g., sum > limit).
'''
# Example: while sum > 10: subtract arr[left], left++

'''

Q3. What is the standard pattern for variable-window problems?
Ans:
Expand with right → Fix violations → Shrink with left → Track answer.
'''
# Example:
# for right in range(n):
#     window_sum += arr[right]
#     while window_sum > target: shrink

'''

Q4. How do you compute window length?
Ans:
length = right - left + 1
'''
# Example: left=0, right=3 → length=4

'''

Q5. Why does the algorithm remain O(n)?
Ans:
Because each pointer moves forward at most once.
'''
# Example: left goes 0→4, right goes 0→4 → total < 2n.

'''

Q6. Why is resetting the window unnecessary?
Ans:
Shrinking makes the window valid again without starting from scratch.
'''
# Example: Instead of restarting sum, remove arr[left].

'''

Q7. What type of problems use variable sliding windows?
Ans:
Longest valid subarray, smallest subarray meeting condition, sum constraints.
'''
# Example: Longest window with sum ≤ X, shortest window with sum ≥ X.
