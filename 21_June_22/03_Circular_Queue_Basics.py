'''
============================================================
Q1. What is the simple meaning of a Circular Queue?
Ans:
A circular queue is a queue where the **end connects back to the front** like a circle.
This helps reuse empty spaces when elements are removed from the front.

# Example:
If front moves ahead, new elements can still be added to earlier positions.

------------------------------------------------------------

Q2. Why do we need a Circular Queue instead of a normal queue?
Ans:
In a normal queue, once the front moves forward, the empty spaces at the front
cannot be reused → **wastes space**.
Circular queue reuses space by wrapping around → **more efficient**.

# Example:
In a size-5 queue, if you remove 3 items, you can still add 3 more at the front.

------------------------------------------------------------

Q3. What is the condition for a circular queue to be FULL?
Ans:
A circular queue is full when:

    (rear + 1) % size == front

This means the next position of rear equals the front.

# Example:
front = 0, rear = 4 in size 5 → next is (4+1)%5 = 0 → full.

------------------------------------------------------------

Q4. What happens during dequeue in a circular queue?
Ans:
• Remove the element at **front**  
• Move front to:  (front + 1) % size  
• If front crosses rear → queue becomes empty

# Example:
front=2 → dequeue → new front = (2+1)%5 = 3

------------------------------------------------------------

Q5. Where are circular queues used in real systems?
Ans:
Circular queues are used where data comes continuously and must reuse space efficiently:
• CPU scheduling  
• Printer/job scheduling  
• Network buffers  
• Streaming data systems  

# Example:
Round-robin CPU scheduler uses a circular queue of processes.

============================================================
'''
