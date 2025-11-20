'''
Q1. What does it mean when we say “numbers are just bits”?
Ans:
It means every number in a computer is stored as a sequence of 0s and 1s.
These tiny 0/1 values are called bits.

• Key idea:
  Computers don’t understand 10 or 7 directly — only their bit versions.
'''
# Example:
# 10 → 1010
# 7  → 0111



'''
Q2. Why do computers use binary (0s and 1s) instead of decimal?
Ans:
Because hardware circuits understand only two states:
• ON  → 1  
• OFF → 0  
Binary matches this perfectly.

• Benefit:
  Fast, reliable, and easy for hardware.
'''
# Example:
# Every operation you do (add, subtract, compare) is done using bits.



'''
Q3. How do bit operations help in Data Structures & Algorithms?
Ans:
Bit operations are extremely fast because they work directly on binary data.
They help with:
• toggling values
• checking conditions quickly
• memory-efficient tricks  
• fast multiplication/division using shifts
'''
# Example:
# x << 1 is the same as x * 2



'''
Q4. What are the basic bitwise operations?
Ans:
Common bit operations include:
• AND (&)
• OR (|)
• XOR (^)
• NOT (~)
• Left shift (<<)
• Right shift (>>)

Each operates directly on individual bits.
'''
# Example:
# 5 & 3 → (0101 & 0011) = 0001



'''
Q5. Why is binary representation important in competitive programming?
Ans:
Because many tricky tasks (subset generation, masks, toggles, fast math)
use binary tricks to achieve huge speed improvements.

• Binary lets us pack multiple states into a single number.
'''
# Example:
# Using bits to represent which items are selected in a subset.



'''
Q6. What is a “bit position”?
Ans:
A bit position refers to the index of a bit in a binary number,
counting from right to left starting at 0.

• Important:
  Position 0 = least significant bit (LSB).
'''
# Example:
# In 1011:
# bit0 = 1, bit1 = 1, bit2 = 0, bit3 = 1



'''
Q7. How do we check if a number’s k-th bit is 1?
Ans:
Use the expression:
(n >> k) & 1

This shifts the bit to the right and checks the last bit.

• Uses AND to isolate just that bit.
'''

# Example 1:
# n = 13, k = 2  (13 in binary = 1101)
# Step 1: write n in binary (4 bits shown):  1101
# Step 2: shift right by k=2 positions:
#         1101 >> 2  -> drop the two rightmost bits:  11
# Step 3: now isolate the last bit by AND with 1:
#         11 (binary) & 1 (binary) = 1
# Step 4: result = 1 -> k-th bit is ON (1)
# Intuition: after shifting, the original k-th bit moved into the 0th position; &1 reads it.

# Example 2:
# n = 10, k = 0  (10 in binary = 1010)
# Step 1: write n in binary (4 bits shown):  1010
# Step 2: shift right by k=0 positions (no shift):
#         1010 >> 0  -> 1010
# Step 3: isolate the last bit by AND with 1:
#         1010 (binary) & 1 (binary) = 0
# Step 4: result = 0 -> k-th bit is OFF (0)
# Intuition: k=0 checks the least significant bit (LSB); here LSB is 0.



'''
Q8. Why are bit tricks memory-efficient?
Ans:
Because a single bit can represent “yes/no” or “true/false” states.
This lets programmers store many flags inside one integer.

• Helps when data is large.
'''
# Example 1:
# Suppose you need to store 5 boolean values:
# is_even, is_positive, is_prime, is_visited, is_active
#
# Without bit manipulation:
# you might store them as 5 separate variables → takes more memory.
#
# With bit manipulation:
# You can store all 5 flags inside ONE integer using bits:
# bitmask = 00011101
# Each bit represents one property.
# This uses only a single integer instead of 5 separate booleans.

# Example 2:
# In graphs or DP problems, you often need to mark many states.
# Example: visited[] array for 10 nodes.
#
# Normal way:
# visited = [False, False, False, ...]   (10 entries)
#
# Bit-efficient way:
# Use 1 integer where each bit indicates visited status:
# visited_mask = 0000000000   (10 bits)
# To mark node 3 as visited: visited_mask |= (1 << 3)
# To check visited: (visited_mask >> 3) & 1
#
# This reduces memory drastically, especially when number of states is large.
