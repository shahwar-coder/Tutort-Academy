'''
66. Plus One
https://leetcode.com/problems/plus-one
'''

from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1, -1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            else:
                digits[i]=0
        return [1] + digits # not writing the below if because : if the loop didn’t return earlier, it means all digits turned to 0, and were all 9 earlier
        # if digits[0]==0:
        #     return [1] + digits

