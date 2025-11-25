'''
Q1. What is the Left–Right pointer pattern used for?
Ans:
It is used on **sorted arrays** to find pairs or solve range problems
by moving one pointer from the left end and one from the right end.
'''
# Example:
# l=0, r=n-1 → move inward based on conditions.



'''
Q2. Why must the array be sorted?
Ans:
Because pointer movement depends on comparing the sum or value.
In a sorted array:
• Increasing left increases the value.
• Decreasing right decreases the value.
This allows controlled movement.
'''
# Example:
# If current sum < target → move left to get a bigger sum.



'''
Q3. How does the Left–Right pattern find a pair with a target sum?
Ans:
Start with l at the start and r at the end:
• If arr[l] + arr[r] == target → found.
• If sum < target → move l forward.
• If sum > target → move r backward.
'''
# Example:
# [1,2,3,4,6,7,8], target=10
# 1+8=9 < 10 → move l



'''
Q4. Why is this approach O(n) instead of O(n²)?
Ans:
Because each pointer moves at most n steps.
We never re-check a pair once it's skipped.
So the entire search finishes in a single pass.
'''
# Example:
# While (l < r): either l++ or r-- every loop.
