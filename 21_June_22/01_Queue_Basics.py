'''
============================================================
Q1. What is the simple meaning of a queue?
Ans:
A queue is a “first come, first served” structure → **FIFO**.
The element that enters first is removed first.

# Example:
People standing in line → the first person leaves first.

------------------------------------------------------------

Q2. What is the difference between enqueue and dequeue?
Ans:
• enqueue(x) → add x to the **end** of the queue  
• dequeue() → remove the item from the **front**

# Example:
Queue: [10,20,30]
dequeue() → removes 10.

------------------------------------------------------------

Q3. Why is using `list.pop(0)` not good for large queues?
Ans:
Because removing from the front of a list shifts all other elements left → **O(n)** time.
This becomes slow when the queue is large.

# Example:
queue.pop(0) → slow for thousands of items.

------------------------------------------------------------

Q4. How does `deque` fix the performance issue?
Ans:
`deque` allows **append()** and **popleft()** in **O(1)** time.
It’s optimized to add/remove from both ends quickly.

# Example:
from collections import deque
queue = deque()
queue.popleft()  # fast

------------------------------------------------------------

Q5. Where are queues commonly used in DSA?
Ans:
Queues are used in:
• BFS (Breadth-First Search)  
• Scheduling tasks  
• Multi-threaded message handling  
• Producer–consumer problems  
• Request processing in servers  

# Example:
BFS uses a queue to process nodes level-by-level.

============================================================
'''
