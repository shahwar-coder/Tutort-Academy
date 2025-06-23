'''
# TAIL CALL

- When a function calls another function and as it's last action then it is a tail call.
- It's like saying, I am done, now just return whatever the other function returns."
- Don't use what the other function returns, simply you have to return it solely, only then it is a tail call.
'''

# Example
'''
- Recursive call is a tail call in the following example
'''

def tail_recc(n):
    return tail_recc(n-1) # this one will be a tail call call because this was the last thing done.

# OR

def f(x): return f(x - 1)

'''
- What is a TCO?
- A TCO= "Tail Call Optimization"
- Some languages reuse the current function's stack frame instead of making new one - hence saving memory.

- Does Python support TCO?
- NO : Python does not support tail call optimisation.
- If you write deeply recursive call in Python you will hit a "RecursionError: maximum recursion depth exceeded"
- Python deliborately avoids TCO inorder to have a simple readable design , also make debugging easier (with tracebacks)
'''
# This will fall in RecurcieError.
def countdown(n):
    if n == 0:
        return "Done!"
    return countdown(n - 1)  # Tail call


# TIPS:
'''
- Avoid deep recursion even in tail-recursive form — Python has a default recursion limit (~1000 frames).
- Convert tail-recursive functions to iterative ones for performance and safety.
- Don’t expect Python to optimize stack usage for recursive functions — it never will.
- Focus on readability and robustness, not low-level stack management in Python.
'''
