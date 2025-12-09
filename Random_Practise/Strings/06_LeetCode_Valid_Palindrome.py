'''
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/description/
'''
'''This Solution is great, looks like two pointers but truely is not, TWO POINTER approach works "IN-PLACE"'''
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         filtered_chars=[]
#         for ch in s:
#             if ch.isalnum():
#                 filtered_chars.append(ch.lower())
#         new_s=''.join(filtered_chars)

#         n=len(new_s)
#         for i in range(n//2):
#             if new_s[i]!=new_s[n-i-1]:
#                 return False
#         return True

'''True Solution, Optimised'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left<right:
            while left<right and not s[left].isalnum():
                left+=1
                
            while left<right and not s[right].isalnum():
                right-=1
                
            if s[left].lower() != s[right].lower():
                return False
            left+=1
            right-=1
        return True


'''
### Problem in Simple Words
Check if a string reads the same **forwards and backwards**,
**ignoring**:
- spaces
- punctuation
- capitalization  
Only **letters and digits** matter.

---

### Core Idea (Two-Pointers, In-Place Check)
We use two pointers:
- **left** starts at the beginning
- **right** starts at the end

We move them **toward each other**, comparing characters as we go.

---

### Handling Non-Alphanumeric Characters
If a character is **not** a letter or number:
- Skip it
- Do **not** compare it  
This handles cases like `"A man, a plan, a canal: Panama"` correctly.

---

### When We Compare Values
Once both pointers land on valid characters:
- Convert to lowercase and check if they match
- If mismatch → not a palindrome → return False

If they match:
- Move both pointers inward and keep checking

---

### Why This Approach Is Good
- **Does not create a new cleaned string**
- Skips unwanted characters **on the fly**
- Uses the original string → true **O(1) extra space**

---

### When We Stop
If pointers cross each other:
- All compared characters matched → return True

---

### Complexity
- **Time:** O(n) → every char visited at most once
- **Space:** O(1) → only two pointer variables used
'''
