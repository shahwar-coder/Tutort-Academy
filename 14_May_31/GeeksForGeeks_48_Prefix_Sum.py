'''
1-D prefix sum
https://www.geeksforgeeks.org/problems/1-d-prefix-sum/1
'''

class Solution:
    def prefSum(self, arr):
        for i in range(1,len(arr)):
            arr[i] = arr[i-1] + arr[i]
        return arr


# Easy-to-Understand Key Points for “1-D Prefix Sum”

# - A prefix sum array stores running totals:
#       prefix[i] = arr[0] + arr[1] + ... + arr[i]

# - Build it in-place:
#     - Start from index 1 (index 0 stays the same)
#     - For each i:
#          arr[i] = arr[i-1] + arr[i]
#       (arr[i-1] already contains the prefix till i-1)

# - After the loop:
#     arr becomes the full prefix sum array.

# - Why prefix sum is useful:
#     - Allows fast range-sum queries in O(1):
#          sum(L..R) = prefix[R] - prefix[L-1]

# - Time Complexity: O(n)
# - Space Complexity: O(1) when done in-place
