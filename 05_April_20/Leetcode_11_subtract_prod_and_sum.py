'''
1281. Subtract prod and sum of digits of an integer
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/
'''

import math
from typing import List
class Solution:
    def convert_to_digits_list(self, n: int)->List[int]:
        """
        Convert number into list of digits
        """
        return list(map(int, str(n)))

    def subtractProductAndSum(self, n: int) -> int:
        """
        Subtract prod and sum
        """
        digits=self.convert_to_digits_list(n)
        return math.prod(digits)-sum(digits)
