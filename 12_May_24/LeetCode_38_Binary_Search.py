'''
704. Binary Search
https://leetcode.com/problems/binary-search/description/
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        low, high = 0, len(nums)-1

        while low<=high:
            mid = low + (high - low)//2
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return -1


# Easy-to-Understand Key Points for “Binary Search”

# - Use binary search only when the array is already **sorted**.
# - Keep two pointers:
#     low  → start of array
#     high → end of array
# - Repeat while low <= high:
#     - Find middle index using: mid = low + (high - low) // 2
#       (safe formula that avoids overflow in other languages)
#     - If nums[mid] == target → return mid
#     - If target > nums[mid] → search in right half → low = mid + 1
#     - If target < nums[mid] → search in left half  → high = mid - 1
# - If pointers cross (no match found), return -1.
# - Time Complexity: O(log n) → halves the search space each step.
# - Space Complexity: O(1) → uses only fixed variables.
