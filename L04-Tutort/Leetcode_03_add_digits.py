'''
258. Add Digits:
https://leetcode.com/problems/add-digits/
'''

class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            num=sum(map(int, list(str(num))))
        return num

# num = sum(int(d) for d in str(num)) # can be used as well
# To make it faster : mathematical sum approach : 

# class Solution:
#     def addDigits(self, num: int) -> int:
#         return 0 if num == 0 else 1 + (num - 1) % 9
