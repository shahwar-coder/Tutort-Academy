def isPowerOfTwo(self, n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0

'''
🧩 Power of Two — Bitwise Logic Explanation

• ✅ Idea: A power of two has **exactly one bit set** in its binary form.
  Examples:
    1  → 0001  
    2  → 0010  
    4  → 0100  
    8  → 1000  

• ⚙️ Operation: (n & (n - 1))
   → Subtracting 1 flips all bits **after** the rightmost set bit (including it).
   → ANDing clears that single set bit.

• 🔍 Example:
   n = 8  → binary 1000  
   n-1 = 7 → binary 0111  
   1000 & 0111 = 0000 → ✅ only powers of two produce 0 here.

• 🧮 For non-powers of two:
   n = 10 → 1010  
   n-1 = 9 → 1001  
   1010 & 1001 = 1000 (≠ 0) → ❌ not power of two.

• ✅ Hence:
   return n > 0 and (n & (n - 1)) == 0
   → True only when n is a positive power of 2.
'''
