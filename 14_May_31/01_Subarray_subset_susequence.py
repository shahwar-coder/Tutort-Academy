'''
Q1. What is a subarray?
Ans:
A subarray is a continuous block of elements taken from an array.
The order must stay the same and no gaps are allowed.
'''
# Example:
# From [1,2,3,4] → valid: [1,2], [2,3,4]
# Invalid: [1,3] (gap → not contiguous)



'''
Q2. How many subarrays does an array of size n contain?
Ans:
Total subarrays = n*(n+1)/2.
Because for each starting index, you can choose multiple ending positions.
'''
# Example:
# n=4 → 4*5/2 = 10 subarrays.



'''
Q3. What is a subsequence?
Ans:
A subsequence keeps the original order but may skip elements.
It does not have to be contiguous.
'''
# Example:
# [1,3], [1,2,4], [] are subsequences
# [3,1] is not (order changed)



'''
Q4. How many subsequences does an array of size n have?
Ans:
A subsequence can either take or skip each element,
so total subsequences = 2^n (including empty).
'''
# Example:
# n=4 → 16 subsequences (15 non-empty).



'''
Q5. What is a subset, and how is it different from a subsequence?
Ans:
A subset ignores order completely (set behavior).
It only cares which elements are selected, not their positions.
'''
# Example:
# {1,3} and {3,1} are the same subset.
# But [1,3] and [3,1] are different sequences.



'''
Q6. How many subsets does a set of size n contain?
Ans:
Subsets also follow take/skip logic,
so they also total to 2^n including the empty set.
'''
# Example:
# n=4 → 16 subsets.



'''
Q7. What is the one-line difference between the three?
Ans:
• Subarray: contiguous + order preserved  
• Subsequence: not contiguous + order preserved  
• Subset: not contiguous + order doesn't matter
'''
# Example:
# [1,3] is a subsequence but not a subarray.
# {1,3} is a subset ignoring order.
