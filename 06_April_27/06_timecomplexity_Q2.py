for (int i = 1; i <= n; i *= c) {
    // constant-time work
}

for (int i = n; i > 0; i /= c) {
    // constant-time work
}
# ==== UNDERSTANDING ====
'''
If a loop multiplies (i *= c) or divides (i /= c) by a fixed number c > 1 each step,
the loop runs about log_c(n) times. We call this O(log n).

- Example: start 1, multiply by 2 until 1024 → 1,2,4,...,1024 which is 10 steps (log2(1024)=10).
- Intuition: multiplying grows or shrinking fast, so you need only a few steps to reach big changes.
- Remember: works when c > 1; constants like c don't change the "log" label in Big-O.
'''

#  ======== SOME QUESTIONS TO SEE, TO SOLIDIFY UNDERSTANDING ========

'''
Q1. What’s the time complexity when a loop multiplies or divides the counter (i *= c or i /= c)?
Ans:
- Such loops run in **O(log n)** time.
- Each iteration grows or shrinks the counter exponentially, not linearly.
'''
# Example:
n = 1024
i = 1
while i <= n:
    i *= 2
# Step-by-step:
# 1, 2, 4, 8, 16, ... 1024 → only ~10 steps (log₂(1024) = 10)
# ✅ Complexity = O(log n)



'''
Q2. Why is it logarithmic, not linear?
Ans:
- Linear growth adds (+c) each step → n steps.
- Logarithmic growth multiplies (*c) each step → only log₍c₎(n) steps.
'''
# Example:
# For n = 1000
# Linear: i += 1 → 1000 iterations
# Logarithmic: i *= 2 → ~10 iterations



'''
Q3. How does division-based looping behave (i /= c)?
Ans:
- Same O(log n) behavior, since each iteration reduces the problem by a constant factor.
'''
# Example:
n = 1024
i = n
while i > 0:
    i //= 2
# Step-by-step:
# 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1 → ~10 steps
# ✅ O(log n)



'''
Q4. Real-world examples of logarithmic loops:
Ans:
✅ Binary search → divides array by 2 each time.  
✅ Tree operations → move down one level each time (height = log n).  
✅ Fast exponentiation (power by squaring) → halves exponent each step.
'''
# Binary search analogy:
low, high = 0, n
while low < high:
    mid = (low + high) // 2
    # Each step halves the range → O(log n)



'''
Q6. Quick summary:
✔ Multiplying/dividing loop counters ⇒ O(log n)
✔ Doubling or halving per iteration grows fast
✔ Base of log doesn’t matter in Big-O
✔ Common in divide-and-conquer and binary algorithms
'''
