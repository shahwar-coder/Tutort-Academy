'''
1004. Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/description/
'''

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''
        Sliding Window, can have max k zeroes (can consider them 1)
        '''
        max_window=0
        zeroes=0
        start=0
        end=0

        for i in range(len(nums)):
            end+=1
            if nums[i] == 0:
                zeroes+=1
            while zeroes>k:
                if nums[start]==0:
                    zeroes-=1
                start+=1
            max_window = max(max_window, end-start)

        return max_window


'''
### Core Idea (Sliding Window)
We want the longest stretch of 1s after flipping at most `k` zeros.
So our sliding window may contain:
- any number of 1s  
- at most `k` zeros (these are the zeros we "pretend" to flip)

### Expanding the Window (Right Pointer)
When moving the right pointer:
- If nums[right] is 1 → window is still valid
- If nums[right] is 0 → increase zero_count (using one flip)

### Shrinking the Window (Left Pointer)
If zero_count becomes greater than k:
- Move the left pointer forward
- If we pass over a 0, decrease zero_count
- Stop shrinking once zero_count ≤ k again

### Measuring Window Size
At each step:
- window_length = end - start
- Since flipping ≤ k zeros is allowed, the full window is valid
- Track the maximum window_length seen so far

### Two Scenarios
1. Window has ≤ k zeros → we can flip all zeros → becomes all 1s  
2. Window has > k zeros → shrink until valid again

### Final Answer
Return the maximum valid window length where zero_count ≤ k.

### Why This Works
A valid answer must come from a stretch containing at most k zeros.
Sliding window checks all such stretches in one pass by expanding and shrinking efficiently.

### Complexity
Time: O(n)  
Space: O(1)
'''
