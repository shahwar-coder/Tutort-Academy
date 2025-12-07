'''
MONOTONIC STACK — Q/A SET

Q1. What is a monotonic stack?
Ans:
A monotonic stack is a stack kept in a single direction (always increasing or always decreasing from bottom → top).
You maintain the order by popping elements that would break the monotonic property before pushing the new one.

# Example:
# To keep an increasing stack: while stack and new_val < stack[-1]: stack.pop()
# Then push new_val.

------------------------------------------------------------

Q2. Why do we pop elements when the monotonic order is broken?
Ans:
Because those popped elements have found a future element (the new_val) that decides their role 
(e.g., their "next greater" or "next smaller").
Popping removes items that cannot remain in the required order and allows the stack to keep only useful candidates.

# Example:
# For next greater: if new_val > stack[-1], then new_val is the next greater for stack[-1] → pop it.

------------------------------------------------------------

Q3. When should we store indices in the monotonic stack instead of values?
Ans:
Store indices when answers depend on positions (distance or index difference), 
e.g. "days to wait" or "index of next greater".
Indices let you compute gaps like (i - j). Values alone can't give these distances.

# Example:
# dailyTemperatures uses indices so ans[j] = i - j when temp[i] > temp[j].

------------------------------------------------------------

Q4. Give the general left→right template for finding Next Greater Element to the Right.
Ans:
Initialize an empty stack (store indices) and ans array (default -1).
For i in 0..n-1:
    while stack and arr[i] > arr[stack[-1]]:
        j = stack.pop()
        ans[j] = arr[i]   # or ans[j] = i for index
    stack.append(i)

This finds the first greater element on the right for each index.

# Tiny example:
# arr = [2,5,3]
# Process 2 → stack=[0]
# Process 5 → pop 0, ans[0]=5; stack=[1]
# Process 3 → stack=[1,2]
# ans = [5,-1,-1]

------------------------------------------------------------

Q5. What is the time complexity of monotonic stack algorithms and why?
Ans:
O(n). Each element is pushed exactly once and popped at most once.
So total push+pop operations across the loop are O(n), making the whole algorithm linear.

# Intuition:
# Although there's a while-loop inside, it does amortized O(1) work per element -> overall O(n).

------------------------------------------------------------
'''
