'''
1961. Check If String Is a Prefix of Array
https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/description/
'''

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        index=0
        for word in words:
            if not s.startswith(word, index):
                return False

            index+=len(word)

            if len(s) == index:
                return True
        return False

# class Solution:
#     def isPrefixString(self, s: str, words: List[str]) -> bool:
#         index=0
#         for word in words:
#             if not s.startswith(word, index):
#                 return False

#             index+=len(word)

#             if len(s) == index:
#                 break
#         return len(s) == index

# Below solution will take more space
# class Solution:
#     def isPrefixString(self, s: str, words: List[str]) -> bool:
#         building_phrase=""
#         for word in words:
#             building_phrase+=word
#             if s == building_phrase:
#                 return True
#         return False

'''
### Problem in Simple Words
You are given:
- a string `s`
- an array of strings `words`

You must check whether `s` can be formed by **joining the first few words from the array in order**.
You cannot skip words or rearrange them.

Example:
- s = "leetcode", words = ["leet","code","hello"] → True
- s = "applepie", words = ["apple","pear","pie"] → False

---

### Core Idea (Match Step-by-Step Using an Index)
Instead of building a new string, we:
- Walk through `s` using an index
- Match each word from `words` **exactly at the current index**

This avoids extra memory and keeps the logic clean.

---

### How the Algorithm Works
- Start with `index = 0` (beginning of string `s`)
- For each `word` in `words`:
    - Check if `s` starts with `word` **at position `index`**
    - If not → mismatch → return False
    - If yes:
        - Move `index` forward by `len(word)`
    - If `index == len(s)`:
        - We matched all characters of `s` exactly → return True

---

### Why `startswith(word, index)` Is Important
- It ensures the word matches **exactly where we are currently pointing**
- Prevents partial or misplaced matches
- Guarantees correct order without concatenation

---

### Why This Approach Is Better Than Building a String
- No extra string creation → memory efficient
- Stops early as soon as a mismatch is found
- Works directly on the original string

---

### Edge Cases Covered
- `s` is shorter than combined words → returns False
- Exact match after a few words → returns True
- Extra words after match → safely ignored

---

### Complexity
- **Time:** O(n), where n = length of `s`
- **Space:** O(1), no extra strings created

---

### Key Insight to Remember
Whenever a problem says:
> “Check if a string is built from prefixes in order”

👉 Think **pointer/index walking**, not string building.
'''
