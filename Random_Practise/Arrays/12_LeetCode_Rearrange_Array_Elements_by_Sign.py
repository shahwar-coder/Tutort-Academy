'''
2149. Rearrange Array Elements by Sign
https://leetcode.com/problems/rearrange-array-elements-by-sign/
'''

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        non_neg_nums = []
        neg_nums = []
        result = []

        # Segregated non-negs and negs
        for num in nums:
            if num>=0:
                non_neg_nums.append(num)
            else:
                neg_nums.append(num)

        # thinking to use zip for corresponding pairs
        for pos, neg in zip(non_neg_nums, neg_nums):
            result.append(pos)
            result.append(neg)
        
        return result

  '''
  ### Problem in Simple Words
You are given an array with:
- equal number of **positive (or zero)** and **negative** numbers

You must rearrange the array so that:
- elements **alternate by sign**
- a **non-negative number comes first**
- the relative order **within positives and negatives is preserved**

Example:
- `[3,1,-2,-5,2,-4]` → `[3,-2,1,-5,2,-4]`

---

### Core Idea (Separate → Then Interleave)
The idea is very simple and clean:
1. **Separate** the numbers by sign
2. **Interleave** them one by one in the required order

This avoids complex index juggling.

---

### How the Solution Works
1. Traverse the array once:
   - Store all non-negative numbers in `non_neg_nums`
   - Store all negative numbers in `neg_nums`
2. Since the problem guarantees equal counts:
   - Use `zip(non_neg_nums, neg_nums)`
3. For each `(pos, neg)` pair:
   - Append `pos`
   - Append `neg`
4. The resulting list automatically follows:
   - non-negative, negative, non-negative, negative…

---

### Why `zip` Is a Good Choice
- It pairs elements **one-to-one**
- Stops automatically at correct length
- Makes the code concise and readable
- Guarantees correct alternation

---

### Why This Approach Is Correct
- Order inside positives is preserved
- Order inside negatives is preserved
- Alternating pattern is guaranteed
- Simple logic, no tricky pointer bugs

---

### Edge Cases Covered
- All constraints guarantee valid input (equal positives & negatives)
- Zero is treated as non-negative (as required)

---

### Complexity
- **Time:** O(n)
- **Space:** O(n) for temporary lists

---

### Key Insight to Remember
Whenever a problem asks for:
> “rearrange elements by categories but preserve order”

👉 Think **segregate first, then merge/interleave**.
  '''
