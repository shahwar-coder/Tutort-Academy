'''
============================================================
Q1. Why can we use a Python list as a stack?
Ans:
Because list supports:
• append() → push  
• pop() → pop  
Both operate at the **end**, so it behaves like a stack.

Example:
stack = []
stack.append(10)
stack.pop()

------------------------------------------------------------

Q2. What is deque and why is it used for stacks?
Ans:
deque (from collections) is a **double-ended queue**.
It gives **fast O(1)** operations for both append() and pop() from ends,
making it very efficient for stack behavior.

Example:
from collections import deque
stack = deque()
stack.append(10)
stack.pop()

------------------------------------------------------------

Q3. What is the performance difference between list and deque?
Ans:
• list.append() → usually O(1)  
• list.pop() → O(1)  

BUT:
If a list becomes very large and needs resizing, operations can get slower.

deque:
• append() and pop() at ends → **always O(1)**  
So deque is **more stable** in performance for big stacks.

------------------------------------------------------------

Q4. When should you prefer list vs deque?
Ans:
Use **list** when:
• Stack is small/medium  
• You only push/pop from the end  

Use **deque** when:
• Stack may grow large  
• You want guaranteed O(1) performance  
• You may push/pop from both ends

------------------------------------------------------------

Q5. Why should you NOT pop/insert at the beginning of a list?
Ans:
Because list operations at index 0 require shifting all elements → O(n).  
deque does this in O(1).  
That’s why deque is preferred for queue-like or double-ended operations.

Example:
list.insert(0, x) → slow  
deque.appendleft(x) → fast
'''
