'''
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/description/
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
      
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         c = Counter(nums)
#         for k,v in c.items():
#             if v>1:
#                 return True
#         return False

'''
### Problem in Simple Words
You are given a list of numbers.
Return **True** if **any number appears more than once**.
Otherwise, return **False**.

---

### Core Idea (Use a Set)
A **set** stores only **unique values**.
So:
- If the list has duplicates → set size becomes smaller
- If all elements are unique → sizes stay the same

---

### How the Check Works
- `len(nums)` → total number of elements
- `len(set(nums))` → number of unique elements

If these two lengths are **not equal**:
→ at least one duplicate exists → return True

---

### Why This Works
- Sets automatically remove duplicates
- Length comparison is a quick and reliable way to detect repetition
- No need to manually count frequencies

---

### Edge Cases Covered
- Empty list → no duplicates → False
- Single element → no duplicates → False
- Multiple repeats → detected immediately

---

### Complexity
- **Time:** O(n)
- **Space:** O(n) for the set

---

### Alternative (When You Need More Control)
Using a frequency map (`Counter`) is useful if:
- You need to know **which** number is duplicated
- You need the **count** of duplicates

But for just checking existence, the set method is the cleanest.
'''
