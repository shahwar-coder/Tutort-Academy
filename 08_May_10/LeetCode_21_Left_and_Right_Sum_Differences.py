'''
2574. Left and Right Sum Differences
https://leetcode.com/problems/left-and-right-sum-differences/
'''

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        nums_length=len(nums)
        leftSum=[0]*nums_length
        rightSum=[0]*nums_length
            
        for i in range(1, nums_length):
            leftSum[i]=leftSum[i-1]+nums[i-1]
                
        for i in range(nums_length-2, -1, -1):
            rightSum[i]=rightSum[i+1]+nums[i+1]
                
        return [abs(l-r) for l,r in zip(leftSum, rightSum)]


# Approach: Left and Right Sum Differences (concise notes + 1 example)

# Key points
# - Build two arrays:
#   * leftSum[i]  = sum of elements strictly left of index i  (sum(nums[:i]))
#   * rightSum[i] = sum of elements strictly right of index i (sum(nums[i+1:]))
# - Compute leftSum in a single left-to-right pass:
#   leftSum[i] = leftSum[i-1] + nums[i-1]
# - Compute rightSum in a single right-to-left pass:
#   rightSum[i] = rightSum[i+1] + nums[i+1]
# - Answer for index i is abs(leftSum[i] - rightSum[i]).
# - Time complexity: O(n). Space: O(n).  
#   (Optional O(1) space: keep total sum and running left sum — shown below.)

# Example (step-by-step)
# nums = [10, 4, 8, 3]
# indices:   0   1   2   3
# n = 4

# 1) Initialize:
#    leftSum  = [0, 0, 0, 0]   # leftSum[0] = 0 by definition
#    rightSum = [0, 0, 0, 0]   # rightSum[n-1] = 0 by definition

# 2) Compute leftSum (left-to-right):
#    i = 1: leftSum[1] = leftSum[0] + nums[0] = 0 + 10 = 10    -> [0, 10, 0, 0]
#    i = 2: leftSum[2] = leftSum[1] + nums[1] = 10 + 4 = 14    -> [0, 10, 14, 0]
#    i = 3: leftSum[3] = leftSum[2] + nums[2] = 14 + 8 = 22    -> [0, 10, 14, 22]

# 3) Compute rightSum (right-to-left):
#    i = 2: rightSum[2] = rightSum[3] + nums[3] = 0 + 3 = 3    -> [0, 0, 3, 0]
#    i = 1: rightSum[1] = rightSum[2] + nums[2] = 3 + 8 = 11   -> [0, 11, 3, 0]
#    i = 0: rightSum[0] = rightSum[1] + nums[1] = 11 + 4 = 15  -> [15, 11, 3, 0]

# 4) Compute absolute differences:
#    index 0: |0  - 15| = 15
#    index 1: |10 - 11| = 1
#    index 2: |14 - 3 | = 11
#    index 3: |22 - 0 | = 22

# Result: [15, 1, 11, 22]
