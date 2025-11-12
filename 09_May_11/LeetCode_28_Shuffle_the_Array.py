'''
1470. Shuffle the Array:
https://leetcode.com/problems/shuffle-the-array/description/
'''

# OPTIMISED
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled=[]
        for i in range(n):
            shuffled.append(nums[i])
            shuffled.append(nums[i+n])
        return shuffled


# ORIGINAL
# class Solution:
#     def shuffle(self, nums: List[int], n: int) -> List[int]:
#         if len(nums)<=1:
#             return nums
#         part1=nums[:n]
#         part2=nums[n:]
#         return [x for pair in zip(part1, part2) for x in pair]
