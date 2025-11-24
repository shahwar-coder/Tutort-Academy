'''
Q1. What do the shift operators << and >> do in binary?
Ans:
<< (left shift) moves bits to the left by k places — new low bits are 0.
>> (right shift) moves bits to the right by k places — high bits depend on type (logical vs arithmetic).

• Short idea:
  Left shift = moves bits left (bigger number usually)  
  Right shift = moves bits right (smaller number usually)
'''
# Left Shift (5 << 1) — simple steps
# 5 = 00000101
# Step 1: Move every bit one place LEFT
#         00000101  →  00001010
# Step 2: The empty rightmost position gets a 0
# Result: 00001010 = 10
# ...............................................

# Right Shift (5 >> 1) — simple steps
# 5 = 00000101
# Step 1: Move every bit one place RIGHT
#         00000101  →  00000010
# Step 2: The rightmost bit (1) falls off
# Result: 00000010 = 2



'''
Q2. Why are shifts often called "multiply/divide by 2" tricks?
Ans:
Because each left shift multiplies by 2, and each right shift divides by 2 (integer division).
This is a very fast CPU instruction used instead of slower multiply/divide in tight code.

• Tip:
  Use shifts when working with exact powers of two for speed.
'''
# 1) Left shift → multiply
# Let n = 7

# n << 3
# means: shift bits left by 3 places
# each left shift = multiply by 2

# Step 1: Multiply by 2 → 7 * 2 = 14
# Step 2: Multiply by 2 → 14 * 2 = 28
# Step 3: Multiply by 2 → 28 * 2 = 56

# So:
# 7 << 3 = 56   (because 7 * 8 = 56)
# ...................................

# 2) Right shift → divide
# Let n = 20

# n >> 2
# means: shift bits right by 2 places
# each right shift = divide by 2 (integer floor)

# Step 1: 20 // 2 = 10
# Step 2: 10 // 2 = 5

# So:
# 20 >> 2 = 5   (because 20 // 4 = 5)



'''
Q3. How do shifts help in DSA/competitive programming for optimisations?
Ans:
• Fast multiply/divide by powers of two (O(1) CPU instruction).  
• Create and combine masks quickly (state compression).  
• Pack several small values into one integer (space efficient).  
• Perform parity, subset, and power-of-two checks cheaply.
'''
# Example:
# Check power of two: (n > 0) and ((n & (n - 1)) == 0)
# Pack two 16-bit values: packed = (a << 16) | b
# Unpack: a = packed >> 16; b = packed & 0xFFFF

