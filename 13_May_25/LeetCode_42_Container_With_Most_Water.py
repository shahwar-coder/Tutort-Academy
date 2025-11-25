'''
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/description/
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_area=0

        while left<right:
            w = right-left
            h = min(height[left], height[right])
            max_area = max(w*h, max_area)

            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
                
        return max_area


# Easy-to-Understand Key Points for “Container With Most Water”

# - The container area is controlled by:
#     width  = distance between pointers
#     height = min(height[left], height[right])
#     area   = width * height

# - Start two pointers:
#     left  = 0               # beginning of array
#     right = n - 1           # end of array

# - At each step:
#     - Compute current area = (right - left) * min(height[left], height[right])
#     - Update max_area if this area is larger.

# - Pointer movement rule:
#     - Move the pointer with the **smaller height**.
#     - Because the height limits the area, and moving the bigger one won’t help.
#     - This greedy decision ensures we explore only the useful possibilities.

# - Stop when both pointers meet.

# - Why two pointers work:
#     - Maximum width starts at ends → best chance for big area.
#     - Only way to get a bigger area is to try for a **taller height**, so move the smaller wall inward.

# - Time Complexity: O(n)  → one pass
# - Space Complexity: O(1) → constant extra memory
