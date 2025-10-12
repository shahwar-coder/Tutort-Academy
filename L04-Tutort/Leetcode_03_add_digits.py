'''
258. Add Digits:
https://leetcode.com/problems/add-digits/
'''

class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            num=sum(map(int, list(str(num))))
        return num
