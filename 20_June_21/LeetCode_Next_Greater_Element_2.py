'''
Next Greater Element II
https://leetcode.com/problems/next-greater-element-ii/
'''

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        next_greater = {}
        stack=[]
        result = [-1] * len(nums)

        for i in range(2 * len(nums)):
            idx = i % len(nums)
            while stack and nums[idx] > nums[stack[-1]]:
                prev_index = stack.pop()
                next_greater[prev_index] = nums[idx]
            stack.append(idx)

        for i in range(len(nums)):
            result[i] = next_greater.get(i, -1)
        
        return result


'''
### Problem in Simple Words
You have a **circular** array.
For each position, find the **first number to the right** (wrapping around if needed)
that is **greater** than the current number.
If none exists → return -1 for that position.

---

### Core Idea (Monotonic Stack + Circular Scan)
We reuse a **monotonic decreasing stack**:
- Stack holds indices of numbers still **waiting** for a greater number.
- When we see a bigger number, it becomes the official “next greater” for that index.

But here the array is **circular**, so:
- We scan the array **twice** to allow elements near the end to look back to the start.
- Circular behavior is simulated using modulo indexing.

---

### How the Stack Logic Behaves
- Move from left → right across the array (twice).
- While the stack has elements and the current number is greater than the number at the top index:
    → We found the next greater element for that top index  
    → Record that relationship and remove the index from the stack
- Push the current index into the stack
  (this index will wait for a future greater number)

Each index gets processed efficiently:
- It is pushed when first seen
- It is popped only if and when a greater number appears

---

### Why We Only Loop Twice
- First loop: find next greater in the usual direction
- Second loop: allow wrapping around so the end elements can check the start
- After two full cycles, everyone has had a chance to find a bigger future number

---

### Why This Works
- A monotonic stack ensures comparisons only happen when needed
- Circular wrap-around is handled smoothly
- Each index gets its answer in the **earliest** possible moment

---

### Final Output Meaning
For each position:
- If a greater number exists later in circular order → we return that number
- If not → we return `-1`

---

### Complexity
- **Time:** O(n) → linear, since each index is pushed & popped at most once
- **Space:** O(n) → for stack + result storage
'''
