'''
Q1. How do computers represent integers internally?
Ans:
- As binary digits (0s and 1s).
- Each bit corresponds to a power of 2.

Example:
'''
n = 13
print(bin(n))  # 0b1101

# Step-by-step:
# 13 in decimal → 8+4+1 → binary digits 1101.



'''
Q2. How do you convert decimal to binary manually?
Ans:
- Divide number by 2 repeatedly.
- Collect remainders, read bottom-up.

Example: 34
'''
# 34 ÷ 2 = 17 remainder 0
# 17 ÷ 2 = 8  remainder 1
# 8 ÷ 2  = 4  remainder 0
# 4 ÷ 2  = 2  remainder 0
# 2 ÷ 2  = 1  remainder 0
# 1 ÷ 2  = 0  remainder 1

# Binary = 100010



'''
Q3. How do you convert binary back to decimal?
Ans:
- Multiply each bit by its place value (power of 2).
- Sum them up.

Example: 100010
'''
# (1 × 2⁵) + (0 × 2⁴) + (0 × 2³) + (0 × 2²) + (1 × 2¹) + (0 × 2⁰)
# = 32 + 2 = 34



'''
Q4. What does Python provide for binary conversions?
Ans:
- bin(n) → binary string.
- int(binary_string, 2) → decimal.

Example:
'''
print(bin(34))        # 0b100010
print(int("100010",2)) # 34



'''
Q5. Why are fixed-size units (8, 16, 32 bits) important?
Ans:
- Limit storage capacity.
- Example: 8-bit unsigned → 0–255.
- Overflow if number too large.

Example:
'''
# 8-bit max = 11111111 → 255
# If we add 1 → wraps (in real hardware).



'''
Q6. Quick shorthand
- Decimal → Binary: divide by 2.
- Binary → Decimal: sum powers of 2.
- Python: bin(), int(...,2).
- Storage uses fixed bits (e.g., 8/16/32/64).
'''
