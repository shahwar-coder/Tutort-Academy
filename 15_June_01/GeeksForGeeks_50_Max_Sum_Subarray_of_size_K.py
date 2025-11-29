'''
Max Sum Subarray of size K
https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1
'''

class Solution:
    def maxSubarraySum(self, arr, k):
        # window_size = k
        window_sum=sum(arr[:k])
        max_sum=window_sum #not zero as sums can be negative, in that 0 will become max, which we do not want
        for i in range(k, len(arr)):
            window_sum = window_sum - arr[i-k] + arr[i]
            max_sum = max(window_sum, max_sum)
        return max_sum


# Easy-to-Understand Key Points for “Max Sum Subarray of Size K”

# - Goal: find the maximum sum of any subarray of fixed size K.

# - Sliding Window idea:
#     - First compute the sum of the initial window (first K elements).
#     - This becomes both window_sum and max_sum.

# - For each step of the window sliding forward:
#     - Remove the element that is leaving the window: arr[i - k]
#     - Add the new element entering the window: arr[i]
#     - Update window_sum accordingly.
#     - Update max_sum if the new window_sum is larger.

# - Why max_sum starts as window_sum (not 0):
#     - Because array values can be negative, and 0 should not override a valid negative max.

# - Time Complexity: O(n)
#     - We compute the first window in O(k) and each slide in O(1).
# - Space Complexity: O(1)
#     - Only constant extra variables used.

