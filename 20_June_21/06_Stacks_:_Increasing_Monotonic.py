'''
INCREASING MONOTONIC STACK — Q/A SET 

------------------------------------------------------------
Q1. What is an increasing monotonic stack?
Ans:
It’s a stack where values (or values pointed by indices) go **up** from bottom → top.
Meaning: bottom ≤ ... ≤ top.
To maintain this, we pop while new_value < stack_top.

# Example pattern:
while stack and new < stack[-1]:
    stack.pop()
stack.append(new)

------------------------------------------------------------

Q2. Why do we use an increasing stack for “next smaller element to the right”?
Ans:
Because when a **smaller** value appears, it becomes the “next smaller” for all larger ones stored on the stack.
Popping exposes elements waiting for a smaller number.

# Tiny example:
arr = [4,2,5]
Process 4 → stack=[4]
Process 2 → pop 4 (next smaller is 2), stack=[2]
Process 5 → push → stack=[2,5]

------------------------------------------------------------

Q3. How does the increasing stack help avoid O(n²) brute force?
Ans:
Instead of checking every pair (i,j), the stack keeps only **useful** candidates.
Any element popped is popped only once.
This reduces total comparisons drastically, giving O(n) time.

# Key idea:
Stack only stores a decreasing history of values.
Useless elements are removed immediately.

------------------------------------------------------------

Q4. Why does the stack usually store indices instead of values?
Ans:
Indices allow you to:
• assign answers to specific positions  
• compute distances (jumps)  
• avoid losing duplicate-value information

# Example:
If arr=[3,1,1], two indices have same value 1 — storing indices keeps them distinct.

------------------------------------------------------------

Q5. Write a small, generic template for “Next Smaller Element to the Right” using an increasing stack.
Ans:
def next_smaller(arr):
    n = len(arr)
    ans = [-1]*n
    stack = []  # indices

    for i in range(n):
        while stack and arr[i] < arr[stack[-1]]:
            j = stack.pop()
            ans[j] = arr[i]
        stack.append(i)

    return ans

# Stack property: arr[stack] is increasing bottom→top.

------------------------------------------------------------
'''
