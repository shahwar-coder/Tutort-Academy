'''
459. Repeated Substring Pattern
https://leetcode.com/problems/repeated-substring-pattern/
'''

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]

        # Points to note:
        # - A repeated string will reappear inside its own doubled version (minus edges).
        # - If s is made by repeating a substring. Then s must appear inside (s + s) after removing first & last chars
        # - First anf Last characters are removed. This removes the trivial full-string match.

# Below is a good solution but time comlexity for worst case is still O(n^2) due to new string formations everytime.
# class Solution:
#     def repeatedSubstringPattern(self, s: str) -> bool:
#         n = len(s)
#         result=""
#         i=1
#         while i<=n//2:
#             sub_str = s[:i]
#             factor = n//i
#             result = sub_str * factor
#             i+=1
#             if result == s:
#                 return True
#         return False

'''
### Problem in Simple Words
You are given a string `s`.
Check if it can be formed by **repeating one of its substrings multiple times**.

Example:
- `"abab"` → `"ab"` repeated → True
- `"aba"` → cannot be repeated → False
- `"aaaa"` → `"a"` repeated → True

---

### Core Idea (Smart String Trick)
If a string is made by repeating a smaller substring, then:
- It will appear **inside its own doubled version** (`s + s`)
- But we must remove the **first and last characters** to avoid a trivial full match

So:
- Check whether `s` exists inside `(s + s)[1:-1]`

If yes → string is built by repetition  
If no → it is not

---

### Why Removing First & Last Characters Is Important
- `s + s` always contains `s` as a full match at the start and end
- Removing the edges forces us to detect only **true internal repetitions**
- This eliminates false positives

---

### Why This Works
- Repeated patterns naturally shift and overlap in the doubled string
- Non-repeated strings cannot fully reappear once edges are removed
- This trick avoids checking every possible substring

---

### Complexity
- **Time:** O(n)
- **Space:** O(n)

---

### Problem in Simple Words
You are given a string `s`.
You must check whether `s` can be formed by **repeating one of its substrings**
multiple times.

Example:
- `"abab"` → `"ab"` repeated → True  
- `"aba"` → cannot repeat a smaller substring → False

---

## Key Points for the **Substring Construction Approach** (Commented Solution)

### Core Idea (Try All Possible Substrings)
If `s` is made by repeating a substring:
- That substring’s length must be a **divisor** of `len(s)`
- The substring must start from index `0`
- Repeating it enough times should recreate the full string

So we:
- Try all possible substring lengths from `1` to `n // 2`
- Check if repeating that substring forms the original string

---

### How the Logic Works
1. Let `n = len(s)`
2. For each possible substring length `i` (from `1` to `n//2`):
   - Take `sub_str = s[:i]`
   - Calculate how many times it must repeat:
     - `factor = n // i`
   - Build a new string by repeating:
     - `sub_str * factor`
3. Compare this newly formed string with `s`
   - If equal → repeated pattern exists → return True
4. If no substring works → return False

---

### Why We Only Check Up to `n//2`
- A repeating substring must be **smaller than the full string**
- Any substring longer than `n//2` can repeat at most once → not useful

---

### Why This Approach Is Correct
- Every valid repeated pattern must start from index `0`
- Trying all possible substring lengths ensures we don’t miss any case
- Direct comparison guarantees correctness

---

### Why This Approach Is Slower
- Each repetition creates a **new string**
- In worst case:
  - We try O(n) substring lengths
  - Each string creation + comparison costs O(n)
- Overall worst-case time: **O(n²)**

---

### When This Approach Is Still Useful
- Easy to understand
- Good for learning / brute-force reasoning
- Works fine for small strings

---

### Complexity
- **Time:** O(n²) in worst case
- **Space:** O(n) due to new string creation

---

### Key Insight to Remember
This method focuses on:
> “Try every possible repeating block and rebuild the string”

It’s intuitive and correct — but **not optimal** compared to the  
`(s + s)[1:-1]` trick, which achieves O(n) time.
'''
