'''
349. Intersection of Two Arrays
https://leetcode.com/problems/intersection-of-two-arrays/
'''

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        n2 = set(nums2)

        for num in nums1:
            if num in n2:
                result.add(num)
        
        return list(result)

# olution below is brute force, not optimised, sol above uses set effectively to make overall sol more optimized.
# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         result = set()
#         for i in range(len(nums1)):
#             for j in range(len(nums2)):
#                 if nums1[i] ^ nums2[j] == 0:
#                     result.add(nums1[i])
#         return list(result)


'''
### Problem in Simple Words
You are given two arrays.
You need to return **all numbers that appear in both arrays**.
- Each number should appear **only once** in the result
- Order does not matter

Example:
- nums1 = [1,2,2,1], nums2 = [2,2] → [2]
- nums1 = [4,9,5], nums2 = [9,4,9,8,4] → [4,9]

---

### Core Idea (Use Sets for Fast Lookup + Uniqueness)
We use **sets** because they:
- Automatically remove duplicates
- Allow very fast membership checking (O(1) average)

---

### How the Optimized Solution Works
1. Convert `nums2` into a set:
   - This makes checking “is this number present?” very fast
2. Loop through each number in `nums1`:
   - If the number exists in the set made from `nums2`:
       → add it to the result set
3. Convert the result set to a list and return it

---

### Why We Use a Set for `nums2`
- Checking `num in nums2_list` would take O(n) time
- Checking `num in nums2_set` takes O(1) time
- This reduces overall time significantly

---

### Why the Result Is Also a Set
- The problem requires **unique values only**
- Set automatically ensures no duplicates in the result

---

### Why This Is Better Than Brute Force
Brute force:
- Compare every element of nums1 with every element of nums2
- Time complexity: O(n × m)

Optimized approach:
- One pass with fast lookups
- Much more efficient for large inputs

---

### Edge Cases Covered
- No common elements → empty list returned
- One or both arrays empty → empty list returned
- Duplicate values in input → handled automatically

---

### Complexity
- **Time:** O(n + m)
- **Space:** O(m + k)
  - m = size of nums2 (set)
  - k = size of intersection set

---

### Key Insight to Remember
Whenever a problem asks for:
> “common elements” + “unique values”

👉 Think **set + membership checking**, not nested loops.
'''
