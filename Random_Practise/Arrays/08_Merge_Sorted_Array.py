'''
88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/description/
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        write = m + n - 1

        while j>=0: # will loop till all nums2 numbers are placed
            if i>=0 and nums1[i]>nums2[j]: # i>0, if imp as nums1 can finish before nums2
                nums1[write]=nums1[i]
                i-=1
            else:
                nums1[write]=nums2[j] # if nums2 is lenthier, then remaining can get copied here
                j-=1
            write-=1

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         for i in range(n):
#             nums1[m+i]=nums2[i]
#         nums1.sort()

'''
### Problem in Simple Words
You are given two **sorted arrays**:
- `nums1` has size `m + n`  
  - First `m` elements are valid numbers  
  - Last `n` elements are empty (0s as placeholders)
- `nums2` has `n` valid numbers  

You must merge `nums2` into `nums1` so that:
- The final `nums1` is **sorted**
- The merge is done **in-place**
- Nothing is returned

---

### Core Idea (Fill from the End)
Since both arrays are already sorted:
- The **largest** numbers are at the **end**
- And `nums1` already has empty space at the end

So instead of merging from the front (which would overwrite values),
we **fill `nums1` from the back**.

---

### How the Pointers Work
We use three pointers:
- `i` → last valid element in `nums1` (`m - 1`)
- `j` → last element in `nums2` (`n - 1`)
- `write` → last position in `nums1` (`m + n - 1`)

At each step:
- Compare `nums1[i]` and `nums2[j]`
- Place the larger value at `nums1[write]`
- Move **only the pointer that was used**
- Decrease `write`

👉 **Key Insight**  
At every step, **either `i` or `j` moves — never both**.  
The pointer that does **not** provide the value stays where it is,  
so its element can still be compared in the next step.

This guarantees:
- No element is skipped
- Every element is placed exactly once


---

### Why the Loop Runs While `j >= 0`
- All elements of `nums2` **must be placed**
- If `nums1` finishes early (`i < 0`):
  - Remaining elements of `nums2` are copied directly
- If `nums2` finishes first:
  - Remaining `nums1` elements are already in correct place

---

### Why This Works
- We never overwrite useful data in `nums1`
- We always place the correct largest value first
- Sorting is preserved naturally

---

### Why This Is Better Than Sorting Again
Alternative approach:
- Copy nums2 into nums1
- Sort nums1

That works but:
- Slower (`O((m+n) log (m+n))`)
- Ignores the fact that arrays are already sorted

This approach:
- Uses the sorted property fully
- Runs in linear time

---

### Complexity
- **Time:** O(m + n)
- **Space:** O(1) (in-place)

---

### Key Insight to Remember
When merging into an array with **extra space at the end**:
👉 **Always merge from the back**, not from the front.

'''
