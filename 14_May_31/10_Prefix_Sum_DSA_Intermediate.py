'''
Q1. What is the key idea behind using prefix sums for subarray problems?
Ans:
Instead of summing each subarray directly, we compare two prefix sums.
The difference between prefix[R] and prefix[L-1] gives the subarray sum.
'''
# Example:
# sum(L→R) = prefix[R] - prefix[L-1]



'''VERY VERY IMPORTANT
Q2. How do prefix sums help find if any subarray has a sum equal to K?
Ans:
Check if:
prefix[i] - K exists earlier in a set or map.
If yes, the subarray between those indices has sum K.
'''
# Example:
# If prefix[i] = 12 and K = 5 → need earlier prefix = 7



'''GOOD TO OBSERVE
Q3. How can prefix sums detect a subarray with sum zero?
Ans:
If two prefix values are equal, the subarray between them has sum zero.
Also if prefix[i] itself is zero, a zero-sum subarray starts at index 0.
'''
# Example:
# prefix = [3, 7, 7, 2] → equal values at index 1 and 2 → subarray (2→2) sums to 0



'''
Q4. Why do we often use a hashmap with prefix sums?
Ans:
A hashmap stores all previous prefix sums, letting us check subarray conditions in O(1).
This avoids scanning the array repeatedly.
'''
# Example:
# map[prefix_sum] = earliest index



'''
Q5. How does prefix-based difference reasoning help in counting subarrays?
Ans:
Every time prefix[i] - K appears as an earlier prefix value,
it means one subarray ending at i has sum K.
'''
# Example:
# If prefix[i]=15 and K=10 → look for earlier prefix=5.



'''
Q6. Why is prefix sum preferred over brute force in subarray problems?
Ans:
Brute force checks all subarrays in O(n²),
but prefix sum with hashing reduces many tasks to O(n).
'''
# Example:
# "Number of subarrays with sum K" becomes linear with prefix + hashmap.



'''
Q7. What is the difference between cumulative sum and prefix sum?
Ans:
They are the same idea: running total from the start.
In DSA, “prefix sum” is the standard term used in subarray formulas.
'''
# Example:
# Both refer to: prefix[i] = prefix[i-1] + nums[i]



'''
Q8. How does prefix sum help detect equal-sum partitions?
Ans:
If prefix[i] equals half of total sum, then the array can be split into equal parts at i.
Prefix sums show where the total becomes half.
'''
# Example:
# nums=[1,2,3,3] → prefix=[1,3,6,9], total=9 (odd) → no equal split.
