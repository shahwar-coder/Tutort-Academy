'''
============================================================
Q1. What is stack underflow?
Ans:
Underflow happens when you try to **pop from an empty stack**.
The stack has nothing to remove.

Tiny example:
stack = []
pop() → ❌ underflow (no element to remove)

------------------------------------------------------------

Q2. What is stack overflow?
Ans:
Overflow happens when you try to **push into a full stack**.
(list in Python grows dynamically, but fixed-size stacks can overflow)

Tiny example:
If stack size limit = 3:
push 1, push 2, push 3, push 4 → ❌ overflow

------------------------------------------------------------

Q3. Why does underflow happen in coding questions?
Ans:
Because you didn’t check if the stack is empty **before popping**.

Example:
if stack:  
    stack.pop()
else:
    # avoid underflow

------------------------------------------------------------

Q4. What are real-life examples of overflow and underflow?
Ans:
Underflow → trying to remove a plate when the plate stack is empty  
Overflow → placing more plates when the rack is already full

------------------------------------------------------------

Q5. How do you prevent overflow/underflow in Python stacks?
Ans:
• Check **is_empty()** before pop  
• If using a fixed-size stack, check **size < capacity** before push  
• Python lists rarely overflow, but logic errors can still create bugs

Example:
if not stack.is_empty():
    stack.pop()
'''
