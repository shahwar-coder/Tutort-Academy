'''
704. Binary Search
https://leetcode.com/problems/binary-search/description/
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        middle_index=len(nums)//2
        while nums:
            if nums[middle_index]==target:
                return middle_index
            elif nums[middle_index]>target:
                nums=nums[:middle_index+1]
            elif nums[middle_index]<target:
                nums=nums[middle_index:]
            print("nums now:", nums)
            middle_index=len(nums)//2
