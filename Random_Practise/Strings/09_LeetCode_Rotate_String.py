'''
796. Rotate String
https://leetcode.com/problems/rotate-string/description/
'''

# OPTIMISED
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s)==len(goal) and goal in (s+s)

# BELOW TWO SOLUTIONS NOT (O(N^2))
# class Solution:
#     def rotateString(self, s: str, goal: str) -> bool:
#         sq=deque(s)
#         goal_q=deque(goal)
#         i=0
#         while i<len(sq):
#             i+=1
#             sq.append(sq.popleft())
#             if sq==goal_q:
#                 return True
#         return False

# ======= These both are n^2 =========

# class Solution:
#     def rotateString(self, s: str, goal: str) -> bool:
#         sq=deque(s)
#         i=0
#         while i<len(sq):
#             i+=1
#             sq.append(sq.popleft())
#             if ''.join(sq) == goal:
#                 return True
#         return False

'''
### Problem in Simple Words
You have two strings: `s` and `goal`.

You can **rotate** `s` by moving the first character to the end any number of times.  
You must check: **Can we turn `s` into `goal` using such rotations?**

Example:  
- `s = "abcde"` → rotations: `"abcde"`, `"bcdea"`, `"cdeab"`, `"deabc"`, `"eabcd"`  
- If `goal` is one of these, answer is `True`.

---

### Core Idea (Smart Trick with s + s)
Key observation:

> If `goal` is a rotation of `s`, then `goal` will always appear as a **substring** of `s + s`.

Example:  
- `s = "abcde"`  
- `s + s = "abcdeabcde"`  
- All rotations of `"abcde"` are inside this:  
  `"abcde"`, `"bcdea"`, `"cdeab"`, `"deabc"`, `"eabcd"`

So we just need to:
1. Check that `s` and `goal` have the **same length**  
   (rotating doesn’t change length)
2. Check if `goal` is a **substring** of `s + s`

If both are true → `goal` is a rotation of `s`.

---

### Why Length Check Is Important
- If lengths differ, rotation is **impossible**.  
  No need to do the substring check at all.

---

### Why This Is Better Than Simulating Rotations
A slower way is:
- Actually rotate `s` one step at a time
- Compare with `goal` after each rotation

That takes:
- Up to `n` rotations
- Each rotation + comparison can cost `O(n)`
- Total ≈ `O(n²)`

The `s + s` trick:
- Builds `s + s` once
- Uses substring search which is `O(n)` (optimized internally)
- Total ≈ `O(n)`

---

### Complexity
- Time: `O(n)`  
- Space: `O(n)` for `s + s`

Simple, clean, and very efficient.
'''
