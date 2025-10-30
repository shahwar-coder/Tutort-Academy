'''
1470. Shuffle the Array:
https://leetcode.com/problems/shuffle-the-array/
'''
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if len(nums)<=1:
            return nums
        part1=nums[:n]
        part2=nums[n:]
        return [x for pair in zip(part1, part2) for x in pair]

# ================ Below is how I solved first but too many variable creations, above one is fantastic ========================

# class Solution:
#     def shuffle(self, nums: List[int], n: int) -> List[int]:
#         if len(nums)<=1:
#             return nums
#         part1=nums[:n]
#         part2=nums[n:]
#         new_nums=[]
#         for i in range(n):
#             new_nums.append(part1[i])
#             new_nums.append(part2[i])
#         return new_nums
