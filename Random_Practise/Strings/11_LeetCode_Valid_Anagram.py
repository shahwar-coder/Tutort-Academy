'''
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/description/
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         s_freq = Counter(s)
#         t_freq = Counter(t)

#         return s_freq == t_freq

'''
### Problem in Simple Words
Two strings `s` and `t` are **anagrams** if:
- They contain **exactly the same characters**
- With **exactly the same frequencies**
- Order does NOT matter  
Example: `"listen"` and `"silent"`

---

### Core Idea
Use a **frequency counter** for both strings and compare them.
If both counters match exactly, the strings are anagrams.

`Counter(s)` → tells how many times each character appears in `s`  
`Counter(t)` → same for `t`

If these two dictionaries are equal → same characters & same counts → anagram.

---

### Why This Works
- An anagram must reuse letters **perfectly**
- Direct comparison of frequency maps guarantees:
  - No extra characters
  - No missing characters
  - No mismatched counts
- Order of characters is fully ignored (as desired)

---

### Edge Cases Covered
- Different lengths → counters won't match → returns False
- Empty strings → both counters empty → returns True
- Mixed characters (letters, digits, symbols) → Counter handles all

---

### Complexity
- Counting both strings: O(n + m)
- Comparing dictionaries: O(k), where k is number of unique characters

Overall: **O(n)** time, **O(1)** space for fixed character set (like ASCII)
'''
