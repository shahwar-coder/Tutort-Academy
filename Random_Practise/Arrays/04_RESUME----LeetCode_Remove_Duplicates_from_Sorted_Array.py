'''
26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write=1
        for read in range(len(nums)):
            if nums[read]!=nums[write]:
                nums[write]=nums[read]
                write+=1
        return write



# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         n=len(nums)
#         i=0
#         uniques = set()
#         while i<n:
#             if nums[i] not in uniques:
#                 uniques.add(nums[i])
#                 i+=1 # move i only unique elem found, do not genrally increase i as we might end up skipping values in nums.
#             else:
#                 del nums[i]
#                 n-=1 # imp to reduce final length
