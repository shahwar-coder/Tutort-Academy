'''
560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/description/
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {0: 1}
        count = 0
        running_sum = 0
        
        for val in nums:
            running_sum += val
            count += prefix_count.get(running_sum - k, 0)
            prefix_count[running_sum] = prefix_count.get(running_sum, 0) + 1
        
        return count


# Easy-to-Understand Key Points for “Subarray Sum Equals K”

# - We want the count of subarrays whose sum = k.

# - Use a running prefix sum:
#       running_sum = sum of elements so far.

# - Key idea:
#     If running_sum - k has been seen before,
#     then a subarray ending at the current index has sum k.

# - Use a dictionary (prefix_count) to store:
#       prefix_sum → how many times it appeared

# - Initialize prefix_count = {0: 1}
#     - This handles subarrays starting from index 0.

# - For each value in nums:
#     1) Update running_sum += val
#     2) Look for (running_sum - k) in prefix_count
#          → these are valid subarrays ending here
#          → add that frequency to count
#     3) Add/update running_sum in prefix_count

# - Final count = total number of subarrays whose sum is k.

# - Time Complexity: O(n)
# - Space Complexity: O(n) for hashmap
