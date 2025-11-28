'''
Use Sliding Window when:
- You need to examine **contiguous** elements in an array/string.
- The window size is **fixed** or **can expand/contract**.
- You want to avoid recomputing sums/counts every time.
- The problem involves finding:
    • max/min sum of a subarray
    • counting subarrays with certain properties
    • longest substring with constraints
    • number of distinct chars/elements in a range

In short: use sliding window when the answer depends on a **continuous segment** and you can update the segment efficiently by adding the new element and removing the old one.
'''
