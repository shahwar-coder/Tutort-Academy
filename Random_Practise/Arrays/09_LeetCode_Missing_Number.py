'''
268. Missing Number
https://leetcode.com/problems/missing-number/
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        actual_sum = sum(nums)
        expected_sum = (n * (n + 1))//2 # including the missing number
        missing_number = expected_sum - actual_sum # common sense, diff -> missing number
        return missing_number

# This one is the 2nd best solution, good but space can still be optimised and made from O(n) to O(1)
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         numbers = set(nums)
#         for i in range(0, len(nums)+1):
#             if i not in numbers:
#                 return i

# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         for number in range(0, len(nums)+1):
#             if number not in set(nums):
#                 return number

# =============

# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         numbers = set(range(len(nums)+1))
#         for n in numbers:
#             if n not in nums:
#                 return n

# ===========
              
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums)
#         for number in range(n+1):
#             if not number in nums:
#                 return number


'''
### Problem in Simple Words
You are given an array containing `n` **distinct numbers**.
The numbers are from the range **0 to n**, but **one number is missing**.
You must find and return that missing number.

Example:
- `[3,0,1]` → missing number = `2`
- `[0,1]` → missing number = `2`

---

### Core Idea (Math Trick: Expected Sum vs Actual Sum)
If **no number were missing**, the sum of numbers from `0` to `n` would be:

0 + 1 + 2 + ... + n = n × (n + 1) / 2


So:
- **Expected sum** = sum of all numbers from `0` to `n`
- **Actual sum** = sum of numbers present in the array

The **difference** between these two sums is exactly the missing number.

---

### How the Solution Works
1. Let `n = len(nums)`
2. Compute:
   - `expected_sum = n × (n + 1) // 2`
3. Compute:
   - `actual_sum = sum(nums)`
4. The missing number is:
   - `expected_sum - actual_sum`

This works because:
- Every number except one appears exactly once
- All other values cancel out in the subtraction

---

### Why This Approach Is Optimal
- Only one pass over the array
- No extra data structures
- Clean mathematical reasoning

---

### Edge Cases Covered
- Missing number is `0`
- Missing number is `n`
- Array in any order

---

### Complexity
- **Time:** O(n)
- **Space:** O(1)

---

### Key Insight to Remember
Whenever you see:
> “numbers from 0 to n with exactly one missing”

👉 Think **sum formula or XOR trick** instead of sets or loops.
'''
