'''
225. Implement Stack using Queues
https://leetcode.com/problems/implement-stack-using-queues/
'''

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for i in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0

  '''
  ### Problem in Simple Words
We need to **build a stack (LIFO)** using **only queue operations** (FIFO).
Stack removes the **most recent** element first.  
Queue removes the **oldest** element first.  
So we must **reorganize the queue** to behave like a stack.

---

### Core Idea
Use ONE queue, but:
- Maintain the newest pushed element always at the **front** of the queue.
- Then:
  - `pop()` = remove from front → correct for stack
  - `top()` = front element → correct for stack

---

### How `push()` achieves this
When we push a new number:
- We add it to the end of the queue
- Then rotate the queue so that the new element moves to the **front**

Example:
push(1) → [1]
push(2) → [1,2] → rotate → [2,1]
push(3) → [2,1,3] → rotate → [3,2,1]


Now the **front** always represents the **stack top**.

---

### Why Rotation Works
It simulates the behavior of a stack by:
- Making the most recent element the first to be removed
- Reordering existing elements behind it

---

### Operations Complexity
- **push**: O(n)  
  (rotating elements takes time)
- **pop**: O(1)  
  (just popleft)
- **top**: O(1)  
  (just peek front)
- **empty**: O(1)

---

### Why This Approach Is Good
- Follows required rule: use only queue operations
- Achieves true **stack behavior**
- Very clean logic: restructure on push, efficient pop and top
'''
