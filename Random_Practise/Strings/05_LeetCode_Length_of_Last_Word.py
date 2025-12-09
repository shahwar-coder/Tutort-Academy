'''
58. Length of Last Word
https://leetcode.com/problems/length-of-last-word/description/
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])


'''
### Problem in Simple Words
We need to return the length of the **last actual word** in a string.
Words are separated by spaces, and the string may have extra spaces at the end.

---

### Core Idea
Use Python string utilities:
1️⃣ `.strip()` → removes trailing & leading spaces  
2️⃣ `.split()` → splits string into words (ignores extra spaces automatically)  
3️⃣ Take the **last word** and measure its length

---

### Why This Works
- It correctly ignores:
  - multiple spaces between words
  - spaces at the end or start
- Splitting ensures we get only real words, not empty strings
- Very concise and fully correct for all valid inputs

---

### Example
Input: `"Hello World  "`  
After strip → `"Hello World"`  
After split → `["Hello", "World"]`  
Last word = `"World"` → length = 5

---

### Complexity
Time: O(n)  → scanning through string once  
Space: O(n) → storing split words
'''
