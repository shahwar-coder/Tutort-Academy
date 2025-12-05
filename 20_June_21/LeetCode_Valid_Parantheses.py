'''
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/description/
'''

class Solution:
    def isValid(self, s: str) -> bool:
        pairs={
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack=[]
        for ch in s:
            if not stack:
                stack.append(ch)
            else:
                if pairs.get(ch) == stack[-1]:
                    stack.pop()
                else:
                    stack.append(ch)
        return len(stack)==0


'''
### Core Idea (Stack for Matching Brackets)
We check if every opening bracket has the **correct matching closing bracket**
in the correct order.  
A **stack** is perfect because the most recently opened bracket must close first.

### Bracket Mapping
Use a dictionary to know which opening matches which closing:
    pairs = {')': '(', '}': '{', ']': '['}

### How It Works Step-by-Step
Go through each character `ch` in string `s`:

- If `ch` is an **opening bracket**:
    → push it onto the stack

- If `ch` is a **closing bracket**:
    → check the top (last added) stack element
    → if it matches the required opening bracket:
         pop the stack (valid match)
      else:
         push (or fail immediately — mismatch)

At the end:
- If stack is empty → all brackets matched correctly → return True  
- If stack still has elements → some openings never closed → return False

### Why This Works
Stack ensures brackets follow **LIFO rule**:
last opened = first closed  
which matches real-world parenthesis matching.

### Complexity
Time: O(n)  
Space: O(n) in worst case (all openings before closings)
'''
