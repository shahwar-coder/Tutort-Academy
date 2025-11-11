'''
682. Baseball Game
https://leetcode.com/problems/baseball-game/description/
'''

import math
class Solution:
    def is_convertible_to_number(self, text: str)->bool:
        try:
            return math.isfinite(float(text)) #True/False
        except ValueError:
            return False

    def calPoints(self, operations: List[str]) -> int:
        record=[]
        for op in operations:
            if self.is_convertible_to_number(op):
                record.append(int(op))
            elif op=="C":
                record.pop()
            elif op=="D":
                record.append(record[-1]*2)
            elif op=="+":
                record.append(record[-1]+record[-2])
        return sum(record)


