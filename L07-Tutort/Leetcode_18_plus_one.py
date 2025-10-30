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


# =========================== Below can be used as well, carry based, benefit, used O(1) space not O(n) like in above case ===================================

# from typing import List

# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         """
#         Increment the number represented by digits by one, returning a new list of digits.
#         Works in O(n) time and O(1) extra space.
#         """
#         for i in range(len(digits) - 1, -1, -1):
#             if digits[i] < 9:
#                 digits[i] += 1
#                 return digits
#             digits[i] = 0
#         return [1] + digits

