'''
27. Remove Element
https://leetcode.com/problems/remove-element/description/
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j=0 # write pointer
        for i in range(len(nums)): # i is read pointer
            if nums[i]!=val:
                nums[j]=nums[i]
                j+=1
        return j


# Easy-to-Understand Key Points for “Remove Element”

# - Goal: remove all occurrences of val *in-place* and return the new length.
# - Use two pointers:
#     i → read pointer (checks every element)
#     j → write pointer (builds the cleaned list)

# - For each element:
#     - If nums[i] != val:
#         - Copy nums[i] to nums[j]
#         - Move j forward
#     - If nums[i] == val:
#         - Skip it (do not copy)

# - After the loop, j = number of kept elements.
# - The array's first j positions now contain the valid filtered values.
# - Time: O(n) because we scan once.
# - Space: O(1) because we modify in-place without extra storage.
