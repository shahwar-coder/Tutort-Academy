'''
Array Leaders
https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1
'''
class Solution:
    def leaders(self, arr):
        leads = []
        n = len(arr)
        maximum = arr[-1] # till will handle negatives
        
        # we will collect the max seen so far from right
        
        for i in range(n-1, -1, -1):
            if arr[i]>=maximum:
                maximum=arr[i]
                leads.append(maximum)
        return leads[::-1]

# Below Solution is correct/brute-force, does O(n^2), very witty but not optimised
# class Solution:
#     def leaders(self, arr):
#         leaders = []
        
#         n=len(arr)
        
#         if n<2:
#             return arr
        
#         # Traverse trrough array
#         for traverser in range(n):
#             i=traverser+1 # i = next index
#             # check till right end, from present index
#             while i<n:
#                 if arr[i] > arr[traverser]:
#                     break
#                 i+=1
            
#             if i==n:
#                 leaders.append(arr[traverser])
                
#         return leaders
                    
            
            
'''
### Problem in Simple Words
An element in an array is called a **leader** if:
- It is **greater than or equal to all elements to its right**
- The **rightmost element is always a leader**

Example:
- `[16, 17, 4, 3, 5, 2]` → leaders = `[17, 5, 2]`

---

### Core Idea (Scan from Right, Track Maximum)
Instead of checking every element against all elements to its right,
we scan the array **from right to left** and keep track of the **maximum seen so far**.

Why this works:
- When moving right → left, everything to the right is already known
- If the current element is ≥ max_so_far, it must be a leader

---

### How the Optimized Solution Works
1. Start from the **rightmost element**
   - It is always a leader
   - Initialize `maximum = arr[-1]`
2. Move left one element at a time:
   - If `arr[i] ≥ maximum`:
       → it is a leader
       → update `maximum`
       → add it to the leaders list
3. Since leaders are collected from right to left:
   - Reverse the list before returning

---

### Why Initializing `maximum = arr[-1]` Is Important
- Handles **negative numbers** correctly
- Ensures first comparison is valid
- Avoids incorrect assumptions like starting from 0

---

### Why This Is Better Than Brute Force
Brute-force approach:
- For each element, scan all elements to its right
- Time complexity: O(n²)

Optimized approach:
- Single pass from right to left
- Time complexity: O(n)

---

### Edge Cases Covered
- Single element array → that element is the leader
- All elements decreasing → all are leaders
- Negative values → handled correctly

---

### Complexity
- **Time:** O(n)
- **Space:** O(k) for leaders list

---

### Key Insight to Remember
Whenever a problem says:
> “compare each element with everything to its right”

👉 Try **reverse traversal + running maximum**
instead of nested loops.
'''
        
