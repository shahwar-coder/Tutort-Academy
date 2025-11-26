'''
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/
'''

# Using Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum=0
        max_sum=float('-inf') # bcz list can have all elements as negative
        for n in nums:
            current_sum = max(n, current_sum+n)
            max_sum = max(current_sum, max_sum)
        return max_sum


# Easy-to-Understand Key Points for “Maximum Subarray” (Kadane’s Algorithm)

# - Goal: Find the largest possible sum of a continuous subarray.

# - Kadane’s idea:
#     - At each number, decide:
#         “Should I start a NEW subarray at this number,
#          or extend the current running subarray?”
#     - This is done with:
#         current_sum = max(n, current_sum + n)

# - Why this works:
#     - If current_sum becomes negative, it only hurts future sums.
#       → So we "reset" by starting fresh at n.

# - Keep track of:
#     current_sum → best subarray ending at the current index
#     max_sum     → best subarray found anywhere

# - max_sum starts as -∞ because all numbers can be negative.

# - One pass through the list is enough.

# - Time Complexity: O(n)
# - Space Complexity: O(1)
