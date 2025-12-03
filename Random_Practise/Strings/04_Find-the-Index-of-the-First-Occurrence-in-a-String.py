'''
28. Find the Index of the First Occurrence in a String
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if needle not in haystack:
#             return -1
#         else:
#             return haystack.index(needle)

'''
### Core Idea
We need to find the **first index** where `needle` appears in `haystack`.

### Using Python’s Built-in Method
Python provides:
    haystack.find(needle)

This returns:
- the starting index of the first occurrence, if found  
- -1 if the substring does not exist

### Why `.find()` Works Perfectly
- It performs exactly what the problem asks for.
- It handles edge cases automatically:
    - needle longer than haystack → returns -1
    - needle empty → returns 0 (problem also expects this behavior)
    - repeated patterns → returns the *first* valid match
- Highly optimized internally (written in C)

### No Need for Manual Looping
Since this problem doesn’t require implementing KMP or other algorithms,
using `.find()` is the simplest and most efficient approach for Python.

### Complexity
Time: O(n + m) internally (Python’s optimized substring search)  
Space: O(1)
'''
