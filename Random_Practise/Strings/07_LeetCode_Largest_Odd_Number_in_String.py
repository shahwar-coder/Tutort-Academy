'''
1903. Largest Odd Number in String
https://leetcode.com/problems/largest-odd-number-in-string/description/
'''

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1, -1):
            if int(num[i])%2!=0:
                return num[:i+1]
        return ""

# class Solution:
#     def largestOddNumber(self, num: str) -> str:
#         num_len=len(num)
#         for i in range(num_len):
#             if int(num[num_len-i-1])%2!=0:
#                 return num[:num_len-i]
#         return ""

'''
### Problem in Simple Words
We are given a string of digits.  
We must return the **largest possible odd number** that can be formed by cutting it from the **left side only**.

Meaning:
- We can only trim digits **from the right end**
- The final digit must be **odd**
- If no odd digit exists → return empty string

---

### Core Idea (Scan from Right)
The **last digit** of a number decides if it's odd or even.
So, to get the **largest odd number**, we:
1️⃣ Start checking digits from the **rightmost end**  
2️⃣ Find the first digit that is **odd**  
3️⃣ Return the substring **from start up to that digit**

This ensures:
- We keep as many digits as possible on the left (making the number largest)
- We guarantee the final digit is odd

---

### Why We Iterate Backwards
If we started from the left:
- We might choose an odd digit too early and lose bigger digits behind it
- Going from the right guarantees the **longest valid prefix**

---

### What If No Odd Digit Exists?
- Then it's impossible to form any odd number
- Return `""`

---

### Complexity
- **Time:** O(n) → one backward scan
- **Space:** O(1) → no extra data structures used
'''
