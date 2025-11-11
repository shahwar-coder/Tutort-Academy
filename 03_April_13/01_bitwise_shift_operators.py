'''
Q1. What does the left shift (<<) operator do?
Ans:
- Moves bits to the left by n positions.
- Equivalent to multiplying by 2ⁿ.

Example:
'''
x = 5      # binary: 0101
print(x << 1, x << 2)

# Step-by-step:
# 5 << 1 → 1010 (binary) = 10
# 5 << 2 → 10100 (binary) = 20




'''
Q2. What does the right shift (>>) operator do?
Ans:
- Moves bits to the right by n positions.
- Equivalent to floor-dividing by 2ⁿ.

Example:
'''
x = 20     # binary: 10100
print(x >> 1, x >> 2)

# Step-by-step:
# 20 >> 1 → 1010 (binary) = 10
# 20 >> 2 → 0101 (binary) = 5



'''
Q3. Why do shifts correspond to multiply/divide by powers of 2?
Ans:
- Each left shift adds a zero to binary → value ×2.
- Each right shift drops lowest bit → value //2.
'''



'''
Q4. What happens if you right shift too far?
Ans:
- Shifting beyond number of bits makes value shrink toward 0.
'''



'''
Q5. Do shifts work on negative numbers?
Ans:
- Yes, but representation is in two’s complement.
- Right shift preserves sign (arithmetic shift).

Example:
'''
x = -8
print(x >> 1)

# Step-by-step:
# -8 in binary (two’s complement) shifted right → -4



'''
Q6. Quick shorthand
- << → multiply by 2ⁿ
- >> → floor-divide by 2ⁿ
- Shifting right too far → 0 (for positives).
- Negatives use two’s complement.
'''

