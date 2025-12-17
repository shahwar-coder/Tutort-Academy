'''
Rotate Array by One.
https://www.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1
'''

#User function Template for python3

class Solution:
    def rotate(self, arr):
        arr.insert(0, arr[-1])
        del arr[-1]
        return arr
        
# Below solution creates a new list, caller may not be clling new list but may be using original list.
# So it is important to change the list in place
# class Solution:
#     def rotate(self, arr):
#         rotated_arr = [arr.pop()]
#         rotated_arr.extend(arr)
#         print(rotated_arr)
#         return rotated_arr


'''
### Problem in Simple Words
You are given an array.
You need to **rotate it to the right by one position**, meaning:
- The **last element moves to the front**
- All other elements shift one position to the right
- The rotation must be done **in-place**

Example:
- `[1, 2, 3, 4, 5]` → `[5, 1, 2, 3, 4]`

---

### Core Idea (In-Place Rotation)
We only need two simple steps:
1. Take the **last element**
2. Put it at the **front** of the array

This achieves the required cyclic rotation.

---

### How the Solution Works
- `arr[-1]` gives the last element
- `arr.insert(0, arr[-1])` inserts it at index 0
- `del arr[-1]` removes the extra copy at the end

After these steps:
- Array is rotated correctly
- The original array is modified in-place

---

### Why In-Place Matters
- Some callers expect the **same array object** to be updated
- Creating a new list may break that expectation
- This solution respects the problem requirement

---

### Why This Works
- Python lists support fast insert/delete by index
- Logic directly matches the definition of cyclic rotation

---

### Complexity
- **Time:** O(n)  
  (inserting at the front shifts elements)
- **Space:** O(1)  
  (no extra array created)

---

### Key Insight to Remember
When a problem explicitly says:
> “Rotate the array in-place”

👉 Always modify the **original list**, not a new one.
'''
