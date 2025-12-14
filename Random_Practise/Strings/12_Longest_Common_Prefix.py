'''
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        current_prefix = strs[0]
        for word in strs:
            while not word.startswith(current_prefix):
                current_prefix = current_prefix[:-1]
        return current_prefix


'''
### Problem in Simple Words
You are given a list of strings.
You need to find the **longest prefix** (starting part of the word)
that is **common to all strings**.
If there is no common prefix, return an empty string.

Example:
- ["flower","flow","flight"] → "fl"
- ["dog","racecar","car"] → ""

---

### Core Idea (Shrink the Prefix)
- Start by assuming the **first word** is the common prefix.
- Compare this prefix with every other word.
- If a word does **not** start with the current prefix:
    → shorten the prefix from the **right**
    → keep checking until it matches or becomes empty.

---

### Why We Reduce From the Right
A prefix must start at index 0.
If it doesn’t match:
- The only way to fix it is to **remove characters from the end**.
- Removing from the front would break the idea of a prefix.

---

### How the Process Flows
1. Take the first string as the initial prefix.
2. For each next string:
    - While that string does NOT start with the prefix:
        - Shorten the prefix by one character.
3. If the prefix becomes empty:
    - No common prefix exists → return "".
4. After checking all strings:
    - The remaining prefix is the answer.

---

### Why This Works
- Any common prefix must be a prefix of the **first string**.
- We only shrink when needed, never expand.
- Once a prefix works for all words, it’s guaranteed to be the longest possible.

---

### Edge Cases Covered
- Only one string → that string itself is the prefix.
- No common prefix → prefix reduces to empty string.
- Strings of different lengths handled naturally.

---

### Complexity
- Time: O(n × m)
  where n = number of strings, m = length of the prefix (shrinking cost)
- Space: O(1)
  only the prefix variable is used.
'''
