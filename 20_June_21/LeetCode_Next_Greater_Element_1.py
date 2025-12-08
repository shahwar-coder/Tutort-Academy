'''
496. Next Greater Element I
https://leetcode.com/problems/next-greater-element-i/
'''

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater_mapping={}
        stack=[]
        result=[-1] * len(nums1)

        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                prev_index=stack.pop()
                next_greater_mapping[nums2[prev_index]] = nums2[i]
            stack.append(i)

        for i in range(len(nums1)):
            result[i] = next_greater_mapping.get(nums1[i], -1)

        return result


'''
### Problem in Simple Words
- nums2 = big array
- nums1 = smaller array whose elements all appear in nums2
- For each number in nums1, we must find:
    → the first number to its **right in nums2** that is **greater** than it
    → if no such number exists, answer is -1

### Core Idea (Monotonic Stack on nums2)
Instead of searching to the right again and again (which is slow),
we scan nums2 **once** and pre-compute:
    number → its next greater number

We use a **stack** that keeps indices of nums2 in a way that
the values in it are in **decreasing order** (top is the smallest).

### Why a Decreasing Stack Works
Think of the stack as:
> "numbers that are still waiting for someone bigger on their right".

When we see a new number nums2[i]:
- If nums2[i] is **greater** than the number at the top of the stack:
    - Then nums2[i] is exactly the **next greater element** for that top number,
      because it is the **first** bigger number we’ve met while moving right.
    - So we:
        - pop that index from the stack
        - create a mapping:
              next_greater_mapping[nums2[popped_index]] = nums2[i]
- We keep popping while the current number is greater than the stack top.
- Then we push the current index i to the stack (it now waits for a bigger number).

Each index:
- is pushed once (when we first see it),
- is popped once (when we find its next greater),
so the total operations are still O(n).

### Why We Store Indices (Not Values) in Stack
- We need to compare actual values: nums2[i] and nums2[stack[-1]]
- Indices let us:
    - access the values
    - also know the direction (right side only, since i increases)

### Building the Final Result for nums1
After finishing the scan of nums2:
- next_greater_mapping holds entries like:
      value_in_nums2 → its next greater value
- For each value x in nums1:
    - Look up:
          result[i] = next_greater_mapping.get(x, -1)
    - If x is not in the mapping, it means there was no greater number
      to its right in nums2 → so answer is -1.

### Why This Method Is Good
- We avoid nested loops (which would be O(n²)).
- Stack + single pass over nums2 gives O(n) building time.
- Then simple lookups for nums1 are O(1) each using the dictionary.

### Complexity
- Time:
    - O(len(nums2)) to build the mapping
    - O(len(nums1)) to build the answer
    → Overall: O(n + m)
- Space:
    - O(len(nums2)) for stack + mapping
'''
