'''
============================================================
Q1. What is a Stack in simple words?
Ans:
A stack is a data structure where the **last item added is the first removed**.
(Like a pile of plates — take from the top)

Tiny example:
push 10 → push 20 → pop → removes 20

------------------------------------------------------------

Q2. What does “LIFO” mean in stacks?
Ans:
LIFO = **Last In, First Out**.
The most recently pushed element is removed first.

Example:
push 5, push 9, pop → removes 9

------------------------------------------------------------

Q3. How do you implement a stack in Python using a list?
Ans:
Use **append()** to push and **pop()** to remove from the top.

Example:
stack = []
stack.append(3)   # push
stack.append(7)
stack.pop()       # removes 7

------------------------------------------------------------

Q4. What does the peek() operation do?
Ans:
peek() returns the **top element** without removing it.

Example:
stack = [10,20,30]
top = stack[-1]   # 30

------------------------------------------------------------

Q5. What real coding problem uses a stack?
Ans:
Checking **balanced parentheses** uses a stack.

Example:
"(())" → push '(' , pop on ')' → balanced → True

------------------------------------------------------------
'''
