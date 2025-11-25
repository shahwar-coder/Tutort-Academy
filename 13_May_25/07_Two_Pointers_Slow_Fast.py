'''
Q1. What is the Slow–Fast two-pointer pattern used for?
Ans:
It is used when one pointer moves quickly (fast)
and the other pointer updates the final result (slow).
'''
# Example:
# fast scans every element, slow writes only unique ones.



'''
Q2. How does Slow–Fast help remove duplicates in a sorted array?
Ans:
fast moves through every element.
Whenever nums[fast] ≠ nums[slow], we copy nums[fast] to slow+1
and move slow forward.
'''
# Example:
# [1,1,2,2,3] → slow builds [1,2,3]



'''
Q3. How is the Slow–Fast pattern used in linked list cycle detection?
Ans:
Fast moves two steps at a time,
slow moves one step at a time.
If they ever meet, a cycle exists.
'''
# ────────────────────────────────────────────────────────
# Example (visual):
# 1 → 2 → 3 → 4 → 5
#           ↑     |
#           |_____|

# Cycle starts at node with value 3.
# Node 5 connects back to node 3.

# ────────────────────────────────────────────────────────
# Step-by-step movement (Phase 1: Detect cycle)

# Iteration 1:
# - slow moves to 2  
# - fast moves to 3  

# Iteration 2:
# - slow moves to 3  
# - fast moves to 5  

# Iteration 3:
# - slow moves to 4  
# - fast moves from 5 → 3 → 4 (two steps)  
# → slow and fast meet at node 4  
# → Meeting point found ⇒ cycle exists.

# ────────────────────────────────────────────────────────
# Phase 2: Find the cycle’s starting node

# Reset:
# - Pointer A starts at head (node 1)  
# - Pointer B starts at meeting point (node 4)

# Move both one step at a time:

# Step 1:
# - A → 2  
# - B → 5  

# Step 2:
# - A → 3  
# - B → 3  
# → Both meet at node 3 ⇒ cycle begins here.

# ────────────────────────────────────────────────────────
# Essence / Key points:

# • Slow moves +1, fast moves +2.  
# • If they meet → guaranteed cycle.  
# • After meeting:  
#   – Put one pointer at head, keep one at meeting point.  
#   – Move both +1 step repeatedly.  
#   – Where they meet again = cycle start.

# • Time: O(n)  
# • Space: O(1)  
# • Works because fast covers the cycle’s extra distance and the math forces a meeting.





'''
Q4. Why is Slow–Fast efficient?
Ans:
Both pointers move forward,
so the total work is still O(n)
with constant extra space O(1).
'''
# Example:
# fast and slow together make only ~n steps.
