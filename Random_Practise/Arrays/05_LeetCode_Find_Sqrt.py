'''
69. Sqrt(x)
https://leetcode.com/problems/sqrtx/description/
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        if x<=1:
            return x

        low, high = 0, x//2
        while low<=high:
            mid = (low+high)//2
            square = mid * mid
            if square == x:
                return mid

            elif mid * mid > x:
                high = mid - 1
            
            else:
                low = mid + 1
        
        return high


'''
### Problem in Simple Words
Given a non-negative integer `x`,
find the **integer part** of its square root.

- You must return ⌊√x⌋ (floor value)
- Decimal part is ignored

Examples:
- x = 4 → 2
- x = 8 → 2 (because √8 ≈ 2.82)
- x = 0 → 0

---

### Core Idea (Binary Search on Answer)
The square root of `x` lies between:
- **0** and **x // 2** (for x > 1)

Instead of trying all numbers,
we **binary search** to find the largest number whose square is ≤ x.

---

### Why Binary Search Works Here
As `mid` increases:
- `mid * mid` also increases
- So the condition “mid² ≤ x” is **monotonic**

That makes it perfect for binary search.

---

### How the Search Proceeds
1. Set search range:
   - `low = 0`
   - `high = x // 2`

2. Pick middle:
   - `mid = (low + high) // 2`

3. Compare:
   - If `mid * mid == x` → exact square root → return `mid`
   - If `mid * mid > x` → mid is too large → search left (`high = mid - 1`)
   - If `mid * mid < x` → mid is too small → search right (`low = mid + 1`)

4. Loop until pointers cross.

---

### Why We Return `high` at the End
When the loop ends:
- `low` has gone **one step too far**
- `high` points to the **largest value whose square is ≤ x**

That is exactly ⌊√x⌋.

---

### Edge Case Handling
- If `x = 0 or 1`, return `x` directly
- Avoids unnecessary computation

---

### Why This Approach Is Good
- No floating-point math
- Precise integer result
- Much faster than linear search

---

### Complexity
- **Time:** O(log x)
- **Space:** O(1)
'''
