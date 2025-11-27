'''
Q1. How do prefix sums help find a subarray with sum = K?
Ans:
Use a hashmap to store prefix sums.
At index i, if (prefix[i] − K) exists in the map,
then the subarray between that earlier index+1 and i has sum K.
'''
# Example:
# prefix[i] = 15, K = 7 → need earlier prefix = 8



'''
Q2. Why do prefix sums help detect zero-sum subarrays?
Ans:
If the same prefix value appears twice,
the subarray between those positions has sum zero.
Also prefix[i] = 0 means a zero-sum subarray starts at index 0.
'''
# Example:
# prefix = [4,7,7,3] → equal values at index 1 & 2 → zero-sum segment (2→2)



'''
Q3. Why combine prefix sums with a hashmap instead of an array?
Ans:
A hashmap stores prefix sums in O(1) and handles any value,
while array-based solutions only work for small, positive ranges.
'''
# Example:
# Subarray sum = K works with negative values because of hashing.



'''
Q4. How does prefix difference logic help count subarrays with sum = K?
Ans:
Every time prefix[i] − K appears as a previous prefix,
it indicates one new subarray ending at i with sum K.
'''
# Example:
# Need prefix[i] - K = earlier prefix value.



'''
Q5. How does prefix sum help in problems like "number of subarrays divisible by M"?
Ans:
Store prefix % M values in a map.
If two prefix sums have the same remainder,
the subarray between them is divisible by M.
'''
# Example:
# prefix mods: [2,5,5,1] → equal 5’s → divisible segment inside.



'''
Q6. Why do prefix sums work even when numbers are negative?
Ans:
Because prefix stores cumulative totals, and differences of totals
still correctly represent subarray sums, regardless of signs.
'''
# Example:
# prefix: [3, -1, 5] still valid → difference gives correct subarray sums.



'''
Q7. How do prefix sums help with “maximum subarray sum” using Divide & Conquer?
Ans:
Prefix sums allow fast calculation of the best crossing subarray
by checking left-prefix maximum and right-prefix minimum.
'''
# Example:
# crossingSum = maxLeftPrefix − minRightPrefix



'''
Q8. What is the major advantage of prefix sums over sliding window?
Ans:
Prefix sums work even when negative numbers appear,
while sliding-window techniques fail when values can go below zero.
'''
# Example:
# sum = K problems with negative values → use prefix, not window.
