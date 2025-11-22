'''
Q1. What does the bitwise AND (&) operator do?
Ans:
Bitwise AND compares two numbers bit-by-bit.
A bit becomes 1 only if BOTH bits are 1. Otherwise it becomes 0.

• Use-case:
  AND is perfect for “filtering” or “keeping only the required bits”.
'''
# Example:
# 13  → 1101
# 11  → 1011
# AND → 1001  (only common 1-bits kept)

# Code:
a, b = 13, 11
print(a & b)   # Output: 9



'''
Q2. Why is & useful in DSA?
Ans:
Because AND is extremely fast (constant time, O(1)).
It helps perform checks, filters, and bit-level decisions without loops.

• Benefit:
  Much faster than %, /, or conditional loops.
'''
# Example:
# Check if number is odd:
# n & 1 → O(1) and faster than n % 2

# Code:
n = 7
print(n & 1)  # 1 → odd



'''
Q3. What is bit masking, and how does AND help?
Ans:
Bit masking means selecting (keeping) specific bits from a number while ignoring the rest.
To do this, we create a "mask" — a number whose bits indicate which positions we want to keep.

AND helps because it only keeps bits where the mask has 1s.
If the mask bit is 0 → that position becomes 0 in the result.
If the mask bit is 1 → that position stays the same as the original number.

• Rule:
    result = number & mask
'''

# Example (keeping last 3 bits):

# Step 1: Create a mask with last 3 bits = 1:
# mask = 0b111 = 7

# Step 2: Take the number:
# number = 29
# In binary: 29 = 11101

# Step 3: Python converts both numbers to binary internally and applies AND:
#     11101   (29)
#   & 00111   (mask)
#   --------
#     00101   (5)

# Step 4: Python converts the result back to decimal → 5

# Code:
num = 29
mask = 7
print(num & mask)   # Output: 5

# ✅ Part1: Why do we need bit masking? (Real Reason)
# Because sometimes we want to focus on only a specific part of the number
# and ignore everything else.
# A mask helps us select exactly which bits matter.
# Think of a mask like a filter:
# You keep what the mask allows
# You hide everything else
# Exactly like sunglasses filter out strong light — a mask filters out unwanted bits.

# ✅ Part2: Why do we need masking? (Concise Summary)

# • To extract only the specific bits we want.
# • To ignore/remove all other bits in the number.
# • To store multiple true/false flags inside one integer (memory-efficient).
# • To read packed or encoded data formats (systems, networking, graphics).
# • To isolate specific fields in hardware registers.
# • To represent/manage subsets efficiently in DSA and DP problems.
# • To perform fast operations like modulo with powers of two.



'''
Q4. How do we check if a number is odd or even using &?
Ans:
Use the expression: n & 1

• If result = 1 → odd  
• If result = 0 → even
'''
# Example:
# 8 & 1 = 0 → even
# 9 & 1 = 1 → odd

# Code:
print(8 & 1)  # 0
print(9 & 1)  # 1



'''
Q5. How do we check if the k-th bit is ON?
Ans:
We create a mask by shifting 1 to the left k times. This mask has only the k-th bit as 1.
Then we AND the number with this mask.

If the result is NOT zero → the k-th bit was ON.

Formula:
    (n & (1 << k)) != 0

Why this works:
• (1 << k) creates a mask where only the k-th bit is 1.
• AND keeps only bits that match the mask.
• If the k-th bit in n is 1, the result will be non-zero.
• If it is 0, the result becomes zero.
'''

# Example:
# Number = 13 → binary: 1101
# Check k = 2 (0-based indexing from right)

# Step 1: Create mask:
# 1 << 2 = 0100   (mask)

# Step 2: AND with number:
#    1101  (13)
#  & 0100  (mask)
#  -------
#    0100  → non-zero → bit is ON

# Code:
n = 13
k = 2
print((n & (1 << k)) != 0)   # True → bit ON



'''
Q7. How does & help check if a number is a power of 2?
Ans:
For powers of 2:
n has only **one** bit set.
n & (n - 1) removes that bit.

If result becomes 0 → number is power of 2.
'''
# Example:
# 8 = 1000
# 7 = 0111
# 8 & 7 = 0000 → power of 2

# Code:
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

print(is_power_of_two(8))  # True
print(is_power_of_two(10)) # False

