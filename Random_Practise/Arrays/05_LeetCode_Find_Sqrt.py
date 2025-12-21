'''
69. Sqrt(x)
https://leetcode.com/problems/sqrtx/description/
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        low, high = 1, x // 2
        while low <= high:
            mid = (low + high) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square > x:
                high = mid - 1
            else:
                low = mid + 1

        return high



'''
### Problem in Simple Words
You are given a non-negative number `x`.
You need to return the **integer part of √x** (square root),
meaning:
- Return the **largest integer** whose square is **≤ x**
- Do NOT use built-in sqrt functions

Example:
- x = 8 → √8 ≈ 2.8 → answer = 2
- x = 16 → √16 = 4 → answer = 4

---

### Core Idea (Binary Search on the Answer)
The square root of `x` lies somewhere between:
- **1** and **x/2** (for x > 1)

We use **binary search** to efficiently find the correct integer.

Why binary search?
- The function `f(n) = n²` is **monotonic** (always increasing)
- This makes it perfect for binary search

---

### How the Search Works
At each step:
1. Pick a middle value `mid`
2. Compute `mid²`
3. Compare `mid²` with `x`

Cases:
- If `mid² == x` → exact square root found → return `mid`
- If `mid² > x` → mid is too big → search left side
- If `mid² < x` → mid is too small → search right side

---

### Why We Return `high` at the End
When the loop ends:
- `low` has crossed over `high`
- `high` points to the **largest number whose square is ≤ x**

This exactly matches the problem requirement:
> “Return the integer square root (rounded down)”

---

### Edge Cases Handled
- x = 0 → return 0
- x = 1 → return 1
- Large x → binary search avoids slow looping

---

### Why This Approach Is Good
- Much faster than checking every number
- Works for very large inputs
- Clean and commonly expected in interviews

---

### Complexity
- **Time:** O(log x)
- **Space:** O(1)

---

### Key Insight to Remember
Whenever you are asked:
- “find the largest value satisfying some condition”
- and the condition is **monotonic**

👉 Think **binary search on the answer**
'''
