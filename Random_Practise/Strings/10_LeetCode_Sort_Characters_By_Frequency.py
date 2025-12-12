'''
451. Sort Characters By Frequency
https://leetcode.com/problems/sort-characters-by-frequency/description/
'''

class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        sorted_c = sorted(c.items(), key=lambda x : (-x[1], x[0])) #1st sort by descending, then sort by ascending # sort by char not req though # sorted func always retuns a list
        return ''.join(k*v for k,v in sorted_c) # here intuitively people put list comprehension [...] but directly generator can be give (on the fly)


'''
### Problem in Simple Words
We must reorder a string so that:
- Characters with **higher frequency** come first
- Characters with **lower frequency** come later  
If two characters have the same frequency, their order doesn't matter for LeetCode.

Example:  
`s = "tree"` → `eetr` or `eert`

---

### Core Idea
1. Count how many times each character appears  
2. Sort characters based on **frequency (descending)**  
3. Rebuild the string by repeating each character according to its count

This is a straightforward **frequency + sorting** pattern.

---

### Why We Use `Counter`
- `Counter(s)` quickly gives us a dictionary:
  `{char: frequency}`
- Counting manually is slower and more error-prone.

---

### Why the Sorting Key is `(-x[1], x[0])`
- `x[1]` = frequency  
  We use `-x[1]` to sort **highest frequency first**  
- `x[0]` = character  
  Used only as a tie-breaker (not required for LeetCode correctness)

Sorting produces something like:
`[('e', 2), ('t', 1), ('r', 1)]`

---

### Why `''.join(k * v for k, v in sorted_c)` Works
- For each `(character, frequency)` pair:
  - `k * v` repeats the character v times  
    e.g., `'e' * 2 = 'ee'`
- Joining them together creates the final string in sorted order.

Using a **generator expression** (not a list) is memory-efficient and clean.

---

### Why This Approach Is Correct
- Sorting by frequency ensures the most common characters come first  
- Repeating characters according to their count preserves correct quantities  
- Exact ordering for ties is irrelevant to the output validity

---

### Complexity
- Counting: O(n)
- Sorting: O(k log k), where k = number of unique characters (≤ 62 typically)
- Building output: O(n)

Total: **O(n log k)** (fast in practice)
'''
