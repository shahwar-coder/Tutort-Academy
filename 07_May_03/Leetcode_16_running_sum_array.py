'''
1480. Running sum of 1d Array
https://leetcode.com/problems/running-sum-of-1d-array/submissions/1815189884/
'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        new_nums=[]
        total=0
        for num in nums:
            total+=num
            new_nums.append(total)
        return new_nums


# Another good way but will be slower for large inputs (but the trickery is more important here)
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        new_nums=[]
        for i in range(len(nums)): # ->last(included)
            new_nums.append(sum(nums[:i+1]))
        return new_nums
