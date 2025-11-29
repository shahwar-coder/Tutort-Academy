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
### Core Idea (Sliding Window)
Use a sliding window that always contains:
- any number of 1s  
- at most one 0 (this is the zero we pretend to delete)

### Expanding the Window (Right Pointer)
When moving the right pointer:
- If nums[right] is 1 → continue
- If nums[right] is 0 → increase zero_count

### Shrinking the Window (Left Pointer)
If zero_count becomes more than 1:
- Move the left pointer forward
- If the left pointer passes a 0, decrease zero_count
- Stop shrinking once zero_count becomes 1 again

### Measuring Window Size
At each step:
- window_length = right - left + 1  
- Because we must delete exactly one element, the effective length is:  
  window_length - 1

Two scenarios:
1. Window has one zero → deleting that zero leaves pure 1s  
2. Window has no zeros → still must delete one element → length decreases by 1  

### Final Answer
Track the maximum value of (window_length - 1) during the scan.

### Why This Works
Any valid answer must come from a stretch containing at most one zero.  
The sliding window efficiently covers all such stretches in one pass.

### Complexity
Time: O(n)  
Space: O(1)
'''
