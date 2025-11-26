'''
Q1. What does prefix[i] store in a prefix-sum array?
Ans:
prefix[i] stores the total sum of nums[0] to nums[i] including both.
'''
# Example:
# nums   = [3, 4, 2]
# prefix = [3, 7, 9]
# prefix[1] = 3 + 4 = 7


'''
Q2. How do you build a prefix-sum array?
Ans:
Set prefix[0] = nums[0], and for every i > 0:
prefix[i] = prefix[i-1] + nums[i]
'''
# Example:
# prefix[2] = prefix[1] + nums[2]



'''
Q3. Why is prefix sum faster than normal summing for ranges?
Ans:
Normal summing may add many numbers each time (O(n)),
but prefix sum uses stored totals to answer in O(1).
'''
# Example:
# Repeated queries like "sum 10→50" become instant.



'''
Q4. What problem patterns commonly use prefix sums?
Ans:
Range-sum queries, number of subarrays with target sum,
finding equal-sum segments, and cumulative scoring problems.
'''
# Example:
# Find number of subarrays with sum = K.
