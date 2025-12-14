'''
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        n=len(nums)
        while i<n:
            if nums[i]==0:
                del nums[i]
                nums.append(0)
                n-=1 # this is the tricky part, after deltiona nd addition , we reduce 'n', so we do not process appened zeroes
            else:
                i+=1
        return
