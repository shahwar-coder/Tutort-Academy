'''
2527. Find Xor-Beauty of Array
https://leetcode.com/problems/find-xor-beauty-of-array/description/
'''

class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        result=0
        for n in nums:
            result = result ^ n
        return result

# FOR UNDERSTANDING THE QUESTION: Brute Force Below
# Main Idea was index triplet combinations, then value at thet index, then apply formula to three values
# class Solution:
#     def xorBeauty(self, nums: List[int]) -> int:
#         result=0
#         nums_length=len(nums)
#         for i in range(nums_length):
#             for j in range(nums_length):
#                 for k in range(nums_length):
#                     result = result ^ ((nums[i] | nums[j]) & nums[k])
#         return result


'''example: NUMS = [3,7,4,9]
(0,0,0): ((3 | 3) & 3) = 3
(0,0,1): ((3 | 3) & 7) = 3
(0,0,2): ((3 | 3) & 4) = 0
(0,0,3): ((3 | 3) & 9) = 1

(0,1,0): ((3 | 7) & 3) = 3
(0,1,1): ((3 | 7) & 7) = 7
(0,1,2): ((3 | 7) & 4) = 4
(0,1,3): ((3 | 7) & 9) = 1

(0,2,0): ((3 | 4) & 3) = 3
(0,2,1): ((3 | 4) & 7) = 7
(0,2,2): ((3 | 4) & 4) = 4
(0,2,3): ((3 | 4) & 9) = 1

(0,3,0): ((3 | 9) & 3) = 3
(0,3,1): ((3 | 9) & 7) = 3
(0,3,2): ((3 | 9) & 4) = 0
(0,3,3): ((3 | 9) & 9) = 9

(1,0,0): ((7 | 3) & 3) = 3
(1,0,1): ((7 | 3) & 7) = 7
(1,0,2): ((7 | 3) & 4) = 4
(1,0,3): ((7 | 3) & 9) = 1

(1,1,0): ((7 | 7) & 3) = 3
(1,1,1): ((7 | 7) & 7) = 7
(1,1,2): ((7 | 7) & 4) = 4
(1,1,3): ((7 | 7) & 9) = 1

(1,2,0): ((7 | 4) & 3) = 3
(1,2,1): ((7 | 4) & 7) = 7
(1,2,2): ((7 | 4) & 4) = 4
(1,2,3): ((7 | 4) & 9) = 1

(1,3,0): ((7 | 9) & 3) = 3
(1,3,1): ((7 | 9) & 7) = 7
(1,3,2): ((7 | 9) & 4) = 4
(1,3,3): ((7 | 9) & 9) = 9

(2,0,0): ((4 | 3) & 3) = 3
(2,0,1): ((4 | 3) & 7) = 7
(2,0,2): ((4 | 3) & 4) = 4
(2,0,3): ((4 | 3) & 9) = 1

(2,1,0): ((4 | 7) & 3) = 3
(2,1,1): ((4 | 7) & 7) = 7
(2,1,2): ((4 | 7) & 4) = 4
(2,1,3): ((4 | 7) & 9) = 1

(2,2,0): ((4 | 4) & 3) = 0
(2,2,1): ((4 | 4) & 7) = 4
(2,2,2): ((4 | 4) & 4) = 4
(2,2,3): ((4 | 4) & 9) = 0

(2,3,0): ((4 | 9) & 3) = 1
(2,3,1): ((4 | 9) & 7) = 5
(2,3,2): ((4 | 9) & 4) = 4
(2,3,3): ((4 | 9) & 9) = 9

(3,0,0): ((9 | 3) & 3) = 3
(3,0,1): ((9 | 3) & 7) = 3
(3,0,2): ((9 | 3) & 4) = 0
(3,0,3): ((9 | 3) & 9) = 9

(3,1,0): ((9 | 7) & 3) = 3
(3,1,1): ((9 | 7) & 7) = 7
(3,1,2): ((9 | 7) & 4) = 4
(3,1,3): ((9 | 7) & 9) = 9

(3,2,0): ((9 | 4) & 3) = 1
(3,2,1): ((9 | 4) & 7) = 5
(3,2,2): ((9 | 4) & 4) = 4
(3,2,3): ((9 | 4) & 9) = 9

(3,3,0): ((9 | 9) & 3) = 1
(3,3,1): ((9 | 9) & 7) = 1
(3,3,2): ((9 | 9) & 4) = 0
(3,3,3): ((9 | 9) & 9) = 9

XOR of all triplet effective values = 9
XOR of all array elements (3 ^ 7 ^ 4 ^ 9) = 9
Verification: equal? True
'''


# ============

'''
# Easy-to-Understand Key Points for “Find XOR-Beauty of Array”

- The problem looks complex in the description, but the final math simplifies a lot.
- The XOR-beauty of the array is simply:
      nums[0] ^ nums[1] ^ nums[2] ^ ... ^ nums[n-1]
- This works because all the extra operations in the original formula cancel out.
- XOR rules that make this work:
    1) x ^ x = 0  → duplicates cancel.
    2) x ^ 0 = x  → does not change the value.
    3) XOR is commutative & associative → order doesn’t matter.
- Loop through the array and XOR every number into “result”.
- Whatever remains at the end is the XOR-beauty.
- Time: O(n)
- Space: O(1)
'''
