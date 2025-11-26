'''
Q1. How is a hash map used to solve the Two-Sum problem in O(n)?
Ans:
Store each number’s value → index in a hash map.
For every x, check if (target − x) already exists.
If yes, we found the pair in O(1) time.
'''
# Example:
# nums=[2,7,11,15], target=9
# When x=7, we find target−x=2 in map → pair found.



'''
Q2. How do hash maps help detect subarrays with a given sum using prefix sums?
Ans:
Use a map to store each prefix sum.
At index i, if prefix[i] − K exists in the map,
then the subarray ending at i has sum K.
'''
# Example:
# prefix[i]=15, K=10 → need earlier prefix=5.



'''
Q3. Why do hash maps help detect zero-sum subarrays?
Ans:
If the same prefix value appears twice,
the subarray between those indices has sum zero.
Also if prefix[i]=0, a zero-sum subarray starts at index 0.
'''
# Example:
# prefix = [4,7,7,2] → equal values at positions 1 & 2.



'''
Q4. What is load factor in a hash map?
Ans:
Load factor = (number of elements) / (size of internal array).
When it becomes too high, the map resizes to keep O(1) operations fast.
'''
# Example:
# 70 items in table size 100 → load factor = 0.7



'''
Q5. Why does resizing help maintain O(1) performance?
Ans:
Resizing increases the number of buckets so that collisions remain low,
keeping chains short and lookup times constant.
'''
# Example:
# Expanding from 100→200 buckets reduces chain lengths.



'''
Q7. Why does hash-map-based counting beat sorting in many problems?
Ans:
Counting with a map is O(n),
while sorting is O(n log n).
Maps avoid rearranging data and do constant-time updates.
'''
# Example:
# Frequency count: map[x] += 1 → instant.



'''
Q8. How do hash maps enable sliding-window problems?
Ans:
They track window frequencies in O(1) time.
As the window moves, update counts for entering and leaving elements.
'''
# Example:
# Longest substring without repeating characters → uses map for last-seen index.
