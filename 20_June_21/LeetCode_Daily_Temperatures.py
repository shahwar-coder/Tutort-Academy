'''
739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures/
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        answer=[]

        for i in range(len(temperatures)):
            # if nothing in stack
            if not stack:
                stack.append(i)
            else: # there is something in stack
                while temperatures[i] > temperatures[stack[-1]]:
                    prev_index = stack.pop()
                    answer.append(i-prev_index)
                    stack.append(i)
        return answer


