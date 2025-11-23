'''
136. Single Number
https://leetcode.com/problems/single-number/description/
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=0
        for num in nums:
            result=result^num
        return result


# Easy-to-Understand Key Points for “Single Number”

# - In the list, every number appears twice except one special number.
# - XOR (^) has two magic rules:
#     1) x ^ x = 0   → a number cancels itself.
#     2) x ^ 0 = x   → starting from zero keeps the value.
# - So if you XOR all numbers together:
#     - All pairs erase each other (because a ^ a = 0).
#     - Only the single number remains.
# - Start with result = 0 and XOR every element into it.
# - Final answer = the number that never got cancelled.
# - Time: O(n) → go through list once.
# - Space: O(1) → only one variable used.
