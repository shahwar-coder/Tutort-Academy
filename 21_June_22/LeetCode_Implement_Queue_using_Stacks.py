'''
232. Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/description/
'''

class MyQueue:

    def __init__(self):
        self.in_stack=[]
        self.out_stack=[]

    def shift(self): # we use shift before pop/peek, we at core reverse order, inorder to force queue behaviour
        if not self.out_stack:
            while self.in_stack: # we put all in_stack stuff in out_stack
                self.out_stack.append(self.in_stack.pop()) # reverses the order

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.shift()
        return self.out_stack.pop()

    def peek(self) -> int:
        self.shift()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


'''
### Problem in Simple Words
We must build a **queue (FIFO)** using **stack operations (LIFO only)**.
Queue removes **first inserted** element first.
Stack removes **most recent** element first.
So we must **reverse the order** when needed.

---

### Core Idea (Use Two Stacks)
We maintain:
- `in_stack`  → stores **new incoming** elements (normal push)
- `out_stack` → used for **popping in correct queue order**

To pop from a queue, the element that came **earliest** must be removed first.
So when `out_stack` is empty:
- We pour everything from `in_stack` → `out_stack`
- This reverses the order, making the oldest element now on top.

---

### Why `.shift()` is Needed
`.shift()` runs **only when needed**:
- If `out_stack` already has elements, no need to move again
- This keeps pop/peek operations **O(1) amortized**

Example flow:
push(1) → in_stack=[1], out_stack=[]
push(2) → in_stack=[1,2], out_stack=[]

pop():
shift → out_stack=[2,1], in_stack=[]
pop → returns 1 ✔ (FIFO behavior)


---

### How Each Operation Works
| Operation | What Happens | Why It Works |
|----------|---------------|--------------|
| push(x)  | push onto `in_stack` | Stack push is easy and fast |
| pop()    | shift if needed, then pop from `out_stack` | Ensures FIFO |
| peek()   | shift if needed, then read top of `out_stack` | See oldest value |
| empty()  | both stacks empty means queue empty | True/False |

---

### Efficiency (Amortized)
- **push:** O(1)
- **pop:** O(1) amortized  
  (because many pushes are reversed once)
- **peek:** O(1) amortized
- **space:** O(n)

---

### Why This Approach Is Great
- Uses only **valid stack operations**
- Maintains **perfect queue order**
- Shift happens **only when necessary**
- Clean logic and optimal for interviews 🚀
'''
