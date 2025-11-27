'''
485. Max Consecutive Ones
https://leetcode.com/problems/max-consecutive-ones/description/
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones=0
        consecutive_ones=0

        for n in nums:
            if n!=0:
                consecutive_ones+=1
            else:
                max_ones=max(consecutive_ones, max_ones)
                consecutive_ones=0
        max_ones=max(consecutive_ones, max_ones)
        return max_ones


'''
# Easy-to-Understand Key Points for “Max Consecutive Ones”

- Goal: find the longest streak of 1s appearing back-to-back.

- Keep two counters:
    consecutive_ones → current streak of 1s
    max_ones         → best (longest) streak found so far

- Loop through each number:
    - If the number is 1:
         consecutive_ones += 1
    - If the number is 0:
         update max_ones with the current streak
         reset consecutive_ones to 0

- After the loop:
    - Check max_ones again (in case the array ends with 1s)

- Final answer = max_ones

- Time Complexity: O(n)
- Space Complexity: O(1)
'''
