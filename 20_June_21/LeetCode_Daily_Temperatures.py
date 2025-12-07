'''
739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures/
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        n=len(temperatures)
        answer=[0]*n

        for i in range(n):
            while stack and temperatures[stack[-1]]<temperatures[i]: # loop till it finds a warmer temperature
                index=stack.pop()
                answer[index]=i-index
            stack.append(i)
        return answer
