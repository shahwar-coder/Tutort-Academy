'''
1796. Second Largest Digit in a String
https://leetcode.com/problems/second-largest-digit-in-a-string/
'''

class Solution:
    def secondHighest(self, s: str) -> int:
        dgts = set()
        for ch in s:
            if ch.isdigit():
                dgts.add(int(ch)) 
        # now we have all unique digits

        # if dgts has 1 or no value, there can be no 2nd largest
        if len(dgts)<=1:
            return -1

        # if control come here, it has sufficient values
        # remove the max digit
        dgts.remove(max(dgts))
        return max(dgts)

# class Solution:
#     def secondHighest(self, s: str) -> int:
#         dgts = []
#         for ch in s:
#             if ch.isdigit():
#                 dgts.append(int(ch))

#         if not dgts:
#             return -1

#         dgts = set(dgts)
#         dgts.remove(max(dgts))

#         if len(dgts)<1:
#             return -1
#         else:
#             return max(dgts)


'''
### Problem in Simple Words
You are given a string that may contain letters and digits.
You need to find the **second largest digit** that appears in the string.
- Digits are from 0 to 9
- Digits must be **distinct**
- If there is no second largest digit → return `-1`

Example:
- `"dfa12321afd"` → digits = {1,2,3} → second largest = 2
- `"abc111"` → only one digit → return -1

---

### Core Idea (Use a Set for Unique Digits)
We only care about:
- **digits**, not letters
- **unique digits**, not duplicates

So the best structure is a **set**:
- Automatically removes duplicates
- Makes it easy to find max values

---

### How the Solution Works
1. Traverse the string character by character
2. If the character is a digit:
   - Convert it to int
   - Add it to a set
3. After traversal:
   - If the set has **0 or 1 element** → no second largest → return -1
4. Otherwise:
   - Remove the **largest digit**
   - The new maximum is the **second largest digit**
   - Return it

---

### Why Removing the Maximum Works
- After removing the largest digit,
- the largest remaining digit is automatically the **second largest overall**
- No sorting is needed

---

### Why This Approach Is Efficient
- Set ensures uniqueness without extra checks
- We scan the string only once
- Operations like `max()` on a small set (digits 0–9) are very fast

---

### Edge Cases Covered
- No digits in string → return -1
- Only one unique digit → return -1
- Multiple same digits → handled by set

---

### Complexity
- **Time:** O(n), where n = length of string
- **Space:** O(1), because at most 10 digits (0–9) can be stored

---

### Key Insight to Remember
Whenever a problem asks for:
> “largest / second largest unique value”

👉 Think **set + remove max**, instead of sorting everything.
'''
