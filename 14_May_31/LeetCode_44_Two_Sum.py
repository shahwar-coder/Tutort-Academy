'''
1. Two Sum
https://leetcode.com/problems/two-sum/
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i, val in enumerate(nums):
            complement = target - val
            if complement in seen:
                return [i, seen[complement]]
            else:
                seen[val]=i



# Easy-to-Understand Key Points for “Two Sum”

# - Goal: find two different indices i and j such that:
#       nums[i] + nums[j] = target

# - Use a hash map (dictionary) to store:
#       value → index where it was seen

# - As you loop through the array:
#     - Current number = val
#     - Its needed partner = complement = target - val
#     - If complement is already in the dictionary:
#          → we found the pair → return [current_index, stored_index]
#     - Else:
#          → store the current number in the dictionary:
#                 seen[val] = i

# - Reason this works:
#     - Hash map gives O(1) lookup.
#     - We identify the correct pair in a single pass.

# - Time Complexity: O(n)  → one scan + constant-time lookups
# - Space Complexity: O(n) → storing at most one index per number
