'''
167. Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        
        while left<right:
            total = numbers[left] + numbers[right]
            if total==target:
                return [left+1, right+1]
            elif total>target:
                right-=1
            else:
                left+=1
        return []



# We Do NOT need Dict as the ARRAY is sorted.
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         seen={}
#         for i, val in enumerate(numbers):
#             complement = target - val
#             if complement in seen:
#                 return sorted([i+1, seen[complement]+1])
#             else:
#                 seen[val]=i



'''
# Easy-to-Understand Key Points for “Two Sum II — Sorted Array”

- The array is already sorted → perfect for the two-pointer technique.

- Start two pointers:
    left  = 0                  # at the start (smallest numbers)
    right = n - 1              # at the end (largest numbers)

- At each step:
    - total = numbers[left] + numbers[right]

    - If total == target:
         → Found the exact pair → return their 1-based indices.

    - If total > target:
         → Sum too large → move right pointer left (right -= 1)
           to try a smaller number.

    - If total < target:
         → Sum too small → move left pointer right (left += 1)
           to try a larger number.

- Two-pointer works because the array is sorted:
    - Moving left pointer increases the sum.
    - Moving right pointer decreases the sum.

- Guaranteed exactly one solution → loop will always find it.

- Time Complexity: O(n)
- Space Complexity: O(1)
'''
