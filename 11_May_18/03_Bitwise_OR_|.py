'''
Q1. What does the bitwise OR (|) operator do?
Ans:
The OR operator compares two numbers bit-by-bit.
A bit becomes 1 if **any** of the two bits is 1.
It becomes 0 only if both bits are 0.
'''
# Example:
# 0101
# 0011
# ---- OR
# 0111   ← sets bits to 1 wherever possible



'''
Q2. Why is OR described as “set bits”?
Ans:
Because OR forces a bit to become 1 if needed.
So it is used to turn ON (set) a particular bit without affecting other bits.
'''
# Example:
# To turn on bit 2 → n | (1 << 2)
# ...............................
# Suppose n = 13
# Binary of 13 → 1101

# Goal:
# Turn ON bit 2 (0-based from right).

# Step 1: Create mask
# mask = (1 << 2)
# 1 << 2 = 4
# Binary: 0100

# Step 2: OR the number with mask
# result = n | mask

# 1101  (13)
# OR
# 0100  (mask)
# ----
# 1101  (13) → bit was already ON, so result stays 13.

# If bit was OFF, OR would have turned it ON.



'''
Q3. How do we use OR to set the k-th bit of a number?
Ans:
Use: n | (1 << k)
This keeps all original bits the same and turns bit k to 1.
'''
# Suppose current subset-mask = 0101
# This means items {0, 2} are included.
# (Remember: bit positions are counted from the RIGHT end, starting at 0.)

# Goal:
# Add item 1 to the subset.

# Step 1: Create mask for item 1
# add_mask = (1 << 1)
# 1 << 1 = 2
# Binary: 0010

# Step 2: OR with the original mask
# new_mask = 0101 | 0010

# 0101   (items {0,2})
# OR
# 0010   (item 1)
# ----
# 0111   (items {0,1,2})

# Result:
# The subset now includes element 1 as well.



'''
Q4. How does OR support DP (Dynamic Programming) with bitmasking?
Ans:
In DP on subsets, OR helps form new states:
new_state = old_state | (1 << element)
It expands the subset by “activating” that element.
'''
# Example:
# Used heavily in DP problems like Travelling Salesman (TSP) using bitmasks.
# ...........................................................................
# Consider a DP on subsets problem (like TSP).
# Suppose current state-mask = 1001
# This means nodes {0, 3} are visited.
# (Bit positions are counted from the RIGHT end, starting at 0.)

# Goal:
# Add/visit node 2.

# Step 1: Create mask for node 2
# add_mask = (1 << 2)
# 1 << 2 = 4
# Binary: 0100

# Step 2: Form next DP state
# new_state = 1001 | 0100

# 1001   (visited nodes {0,3})
# OR
# 0100   (node 2)
# ----
# 1101   (visited nodes {0,2,3})

# Result:
# DP transitions to a new state representing a larger visited set.
