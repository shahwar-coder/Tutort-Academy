'''
DECREASING MONOTONIC STACK — Q/A SET 

------------------------------------------------------------
Q1. What is a decreasing monotonic stack?
Ans:
A decreasing stack is one where values go **down** from bottom → top.
Meaning: bottom ≥ ... ≥ top.
To maintain this order, we pop while new_value > stack_top.

# Template:
while stack and new > stack[-1]:
    stack.pop()
stack.append(new)

------------------------------------------------------------

Q2. Why do we use a decreasing stack for “Next Greater Element to the Right”?
Ans:
Because when a **bigger** value appears, it becomes the next greater for all smaller values stored at the top of the stack.
We pop those smaller values and assign their answer immediately.

# Example:
arr = [2,5,3]
Process 2 → stack=[2]
Process 5 → pop 2 (next greater is 5), stack=[5]
Process 3 → push → stack=[5,3]

------------------------------------------------------------

Q3. How is a decreasing stack used in the Daily Temperatures problem?
Ans:
The stack stores **indices** of temperatures in **decreasing order**.
When a warmer day (temp[i]) appears, it pops all colder days — meaning their “wait time” is known.
For each popped index j:
    ans[j] = i - j

# So stack top is always the coldest pending day.

------------------------------------------------------------

Q4. Why does a decreasing stack give O(n) time even with a while loop inside?
Ans:
Each index:
• is pushed once  
• is popped at most once  
So even though there’s a while-loop, total work is 2n → O(n).

# Key reason:
No element is re-processed; pops are limited.

------------------------------------------------------------

Q5. Write the common template for the Next Greater Element to the Right using a decreasing stack.
Ans:
def next_greater(arr):
    n = len(arr)
    ans = [-1]*n
    stack = []  # store indices

    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            j = stack.pop()
            ans[j] = arr[i]     # next greater for j
        stack.append(i)

    return ans

# Stack property: arr[stack] decreases bottom→top.

------------------------------------------------------------
'''
