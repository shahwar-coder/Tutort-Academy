'''
66. Plus One
https://leetcode.com/problems/plus-one/
'''

from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int(''.join(map(str, digits)))
        number+=1
        return list(map(int, list(str(number))))
