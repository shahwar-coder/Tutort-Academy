'''
169. Majority Element
https://leetcode.com/problems/majority-element/description/
'''

# Original Solution
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elem_map = {}
        n=len(nums)
        for number in nums:
            if number not in elem_map:
                elem_map[number] = 1
            else:
                elem_map[number] = elem_map.get(number) + 1

        for k,v in elem_map.items():
            if v>n//2:
                return k

# Boyer–Moore Voting Algorithm. , O(1) Space
# count = 0
# candidate = None

# for num in nums:
#     if count == 0:
#         candidate = num
#     count += 1 if num == candidate else -1

# return candidate


'''
### Problem in Simple Words
You are given a list of numbers.
One number appears **more than half of the time** (`> n/2`).
That number is called the **majority element**.
You must return that number.

Example:
- `[3,2,3]` → `3`
- `[2,2,1,1,1,2,2]` → `2`

---

### Core Idea (Counting Frequencies)
If a number appears more than `n // 2` times,  
we can simply **count how many times each number appears**.

Steps:
1. Count frequency of every number.
2. Find the number whose count is greater than `n // 2`.

---

### How the Solution Works
- Use a dictionary (`elem_map`) to store:
number → how many times it appears

- Loop through the array and update counts.
- After counting:
- Check each `(number, frequency)`
- If `frequency > n // 2`, return that number.

---

### Why This Works
- The problem **guarantees** that a majority element exists.
- So exactly **one number** will satisfy `count > n // 2`.
- Dictionary gives fast O(1) average-time updates and lookups.

---

### Edge Cases Covered
- Single element array → that element is the majority.
- All same elements → obvious majority.
- Mixed values → counting handles it safely.

---

### Complexity
- **Time:** O(n)
- One pass to count
- One pass to find majority
- **Space:** O(n)
- Dictionary may store all unique numbers
'''


# b's algorithm
# ### Core Idea (Boyer–Moore Voting Algorithm)
# Instead of counting frequencies, we use a **voting idea**.

# Think of it like this:
# - Same numbers **support each other**
# - Different numbers **cancel each other out**
# - Since the majority element appears more than all others combined,
#   it can never be fully cancelled

# ---

# ### How the Algorithm Thinks (Intuition)
# We keep:
# - `candidate` → the current possible majority element
# - `count` → how strong its support is

# We scan the array once:
# - If `count == 0`:
#     → pick the current number as the new candidate
# - If current number == candidate:
#     → increase count (support)
# - Else:
#     → decrease count (cancel out)

# ---

# ### Why Cancellation Works (The “Magic”)
# Every time we see:
# - one majority element
# - and one non-majority element

# They **cancel each other**.

# Because the majority element appears **more than n/2 times**:
# - After all cancellations,
# - the majority element is the **only one left standing** as the candidate

# ---
