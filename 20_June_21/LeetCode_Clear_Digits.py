'''
3174. Clear Digits
https://leetcode.com/problems/clear-digits/description/
'''

class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for ch in s:
            if not ch.isdigit():
                stack.append(ch)
            else:
                if stack:
                    stack.pop()
        return "".join(stack)


'''
### Core Idea (Use Stack to Remove Characters)
We scan the string from left → right.
- When we see a **letter** → push it into the stack (keep it).
- When we see a **digit** → delete the **most recent letter** by popping the stack.

Digits do **not** stay in the final answer.
They only trigger removal of a previous character.

### How It Works Step-by-Step
For each character `ch` in the string:
- If `ch` is NOT a digit:
    → add it to stack (it’s a valid character)
- If `ch` IS a digit:
    → remove the last character from stack (if stack not empty)

After processing all characters:
- Stack contains only the remaining letters in correct order
- Convert list → string using `"".join(stack)`

### Why Use a Stack?
- Stack naturally follows **Last In, First Out** behavior
- The most recent valid character is removed first by digits
- This exactly matches the problem rule

### Edge Cases Covered
- If a digit appears and stack is empty → ignore (nothing to delete)
- Multiple digits remove multiple previous characters
- Only letters remain in final output

### Complexity
Time: O(n) → process each character once  
Space: O(n) → stack may store up to all letters
'''
