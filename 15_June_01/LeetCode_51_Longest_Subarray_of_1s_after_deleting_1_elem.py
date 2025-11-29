'''
1493. Longest Subarray of 1's After Deleting One Element
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/
'''

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        '''
        This is a sliding window problem where the window may contain at most 1 zero, because you're allowed to delete one element.
        '''
        max_window_size=1
        start=0
        end=0
        zeroes=0

        for i in range(len(nums)):
            end+=1

            if nums[i]==0:
                zeroes+=1

            while zeroes>1:
                if nums[start]==0:
                    zeroes-=1
                start+=1

            max_window_size = max(max_window_size, end-start)

        return max_window_size-1


'''
# Easy-to-Understand Key Points for
# “Longest Subarray of 1s After Deleting One Element”

- You must delete exactly one element.
  → So the final subarray can contain at most **1 zero** within the window.
  → Sliding Window fits perfectly.

- Maintain a window [start … end) with:
      zeroes = number of zeros inside the window
      max_window_size = longest valid window seen so far

- Expand the window from the right:
      if nums[i] == 0:
          zeroes += 1

- If the window becomes invalid (zeroes > 1):
      → shrink from the left until zeroes ≤ 1 again

- Window size formula:
      current_window = end - start
  (end is incremented manually, keeping half-open interval convention)

- Why final result is max_window_size - 1:
      - Because the problem REQUIRES deleting one element.
      - If the window had only 0 zeros, deletion removes one '1'.
      - If the window had 1 zero, deletion removes that zero.
      - So final usable length = window_length - 1.

- Why the algorithm works:
    - The sliding window always maintains the *best possible* streak
      where only a single delete is needed to make it all 1s.
    - We explore each index only once → O(n).

- Time Complexity: O(n)
- Space Complexity: O(1)
'''
