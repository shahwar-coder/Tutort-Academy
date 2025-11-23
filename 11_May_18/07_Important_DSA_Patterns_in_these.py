'''
Q1. How do we quickly check if a number is odd or even using bitwise ops?
Ans:
Use x & 1.
If the result is 1 → odd.
If the result is 0 → even.
'''
# Example:
# 7 & 1 = 1 → odd
# 8 & 1 = 0 → even



'''
Q2. How do we check whether the k-th bit of a number is ON?
Ans:
Use: x & (1 << k)
If result ≠ 0 → the k-th bit is ON.
'''
# Example:
# x = 13 (1101)
# Check bit 2 → 1101 & 0100 = 0100 → ON



'''
Q3. How do we set (turn ON) the k-th bit of a number?
Ans:
Use: x | (1 << k)
This turns the k-th bit to 1 without changing other bits.
'''
# Example:
# To set bit 3:
# x = 0001
# x | 1000 = 1001



'''
Q4. How do we clear (turn OFF) the k-th bit?
Ans:
Use: x & ~(1 << k)
NOT (~) flips the mask, AND clears that specific bit.
'''
# Example:
# Clear bit 2:
# mask = ~(0100) = ...1011
# x & ...1011 → bit 2 becomes 0



'''
Q5. How do we extract the lowest set bit of a number?
Ans:
Use: x & -x
This isolates the rightmost 1-bit.
'''
# x = 101100

# Step 1: Find -x (two’s complement)
#      invert:  010011
#      add 1 →  010100

# Step 2: AND with original
#      101100
# AND  010100
# =    000100

# Result:
# lowest set bit = 000100  (bit position 2)



'''
Q6. How do we count set bits quickly?
Ans:
Use Brian Kernighan’s trick:
Repeat: n &= (n - 1)
Each step removes the lowest set bit.
'''
# Example:
# For 13 (1101):
# 1101 → 1100 → 1000 → 0000 → 3 steps → 3 set bits

# CODE:
def count_bits(n):
    count = 0
    while n:
        n &= (n - 1)   # removes lowest set bit
        count += 1
    return count

print(count_bits(13))  # Output: 3



'''
Q7. How do we test if a number is a power of 2?
Ans:
A power of 2 has exactly one set bit.
So check: (n & (n - 1)) == 0
Be sure that n > 0.
'''
# Example:
# 8 = 1000 → 8 & 7 = 0 → power of 2
# 10 = 1010 → 10 & 9 ≠ 0 → not a power of 2
