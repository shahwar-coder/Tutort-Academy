'''
Q1. What does prefix[i] represent in a prefix-sum array?
Ans:
prefix[i] stores the total sum of arr[0] to arr[i] (inclusive).
'''
# Example:
# arr = [2,3,5]
# prefix[1] = 2 + 3 = 5
# So basically till index i it holds the sum till there.



'''
Q2. How do you build a prefix-sum array?
Ans:
Set prefix[0] = arr[0].  
For every i > 0:
prefix[i] = prefix[i-1] + arr[i]
'''
# Example:
# prefix[2] = prefix[1] + arr[2]



'''
Q3. What is the formula to find the sum from index L to R?
Ans:
If L == 0:
    sum = prefix[R]
Else:
    sum = prefix[R] - prefix[L-1]
'''
# Example:
# sum(1→3) = prefix[3] - prefix[0]



'''
Q4. Why does prefix sum make range-sum queries faster?
Ans:
Because we reuse stored totals instead of adding each element again.
This reduces the time from O(n) to O(1).
'''
# Example:
# Multiple queries like sum(0→2), sum(2→5) become instant.



'''
Q5. What common problem types use prefix sum?
Ans:
Range sums, subarray problems, frequency counting,
and any task needing repeated sum queries.
'''
# Example:
# “Find sum of each subarray of length 3.”



"""
Q. How do you build a prefix-sum array?
Ans:
Set prefix[0] = arr[0].
For every i > 0:
prefix[i] = prefix[i-1] + arr[i]
"""

# Example in Python:
arr = [2, 4, 6, 1]

prefix = [0] * len(arr)
prefix[0] = arr[0]

for i in range(1, len(arr)):
    prefix[i] = prefix[i-1] + arr[i]

print("Array:         ", arr)
print("Prefix Sum:    ", prefix)
# Example: prefix[2] = prefix[1] + arr[2] → 6 + 6 = 12



"""
Q7. Why does prefix sum work mathematically?
Ans:
prefix[R] includes all values from 0→R.
prefix[L-1] includes 0→L-1.
Subtracting removes the earlier part, leaving L→R.
"""

# Example in Python:
arr = [3, 5, 2, 8, 1]   # indices: 0  1  2  3  4

# Build prefix sum
prefix = [0] * len(arr)
prefix[0] = arr[0]
for i in range(1, len(arr)):
    prefix[i] = prefix[i-1] + arr[i]

# Query sum from L=1 to R=3 → elements = 5 + 2 + 8 = 15
L, R = 1, 3
range_sum = prefix[R] - (prefix[L-1] if L > 0 else 0)

print("Array:       ", arr)
print("Prefix Sum:  ", prefix)
print(f"Sum {L}→{R}:", range_sum)
# Explanation:
# prefix[3] = sum(0→3)
# prefix[0] = sum(0→0)
# prefix[3] - prefix[0] = (0→3) - (0→0) = (1→3)

