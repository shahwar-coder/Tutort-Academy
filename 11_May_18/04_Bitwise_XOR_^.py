'''
Q1. What does the XOR (^) operator do?
Ans:
XOR compares bits of two numbers.
A bit becomes 1 only if the bits are DIFFERENT.
If the bits are the same (0-0 or 1-1), the result is 0.
'''
# Example:
# 0101
# 0011
# ---- XOR
# 0110



'''
Q2. Why is XOR called a “toggle” operator?
Ans:
Because XOR with 1 flips (toggles) a bit, and XOR with 0 keeps it unchanged.
'''
# Example:
# bit ^ 1 → toggles
# bit ^ 0 → unchanged

# ......................

# XOR truth:
# bit ^ 1 → toggles the bit
# bit ^ 0 → keeps the bit unchanged

# Suppose n = 1011 (binary)
# We want to toggle bit 2 (counting from RIGHT, starting at 0).

# Step 1: Create toggle mask
mask = (1 << 2)     # 0100

# Step 2: Apply XOR
result = n ^ mask

# 1011   (initial number)
# XOR
# 0100   (toggle bit 2)
# ----
# 1111   (bit 2 flipped from 0 → 1)

# If the bit was already 1, XOR would flip it to 0.



'''
Q1. How does XOR help *remove duplicates* (find the single unique element)?
Ans:
XOR cancels identical numbers because x ^ x = 0 and x ^ 0 = x. 
If every element appears twice except one, XORing the whole array leaves the unique element.
'''
# Array: [4, 1, 2, 1, 2]
# Goal: find the element that appears once.

# Step 1: Start with result = 0
result = 0

# Step 2: XOR each element into result
result = result ^ 4   # 0 ^ 4 = 4
result = 4 ^ 1        # = 5
result = 5 ^ 2        # = 7
result = 7 ^ 1        # = 6  (because 7 ^ 1 = (4^1) ^ 2 ^ 1 = 4 ^ (1^1) ^ 2 = 4 ^ 0 ^ 2 = 6)
result = 6 ^ 2        # = 4  (2 cancels with earlier 2)

# Final result = 4  → the unique element.



'''
Q2. How does XOR’s commutative & associative property help in algorithms?
Ans:
Because order doesn't matter (a ^ b = b ^ a) and grouping doesn't matter, 
you can rearrange XOR operations to cancel pairs or simplify expressions.
'''
# Expression: 5 ^ 3 ^ 5 ^ 7
# Step 1: Group duplicates using commutativity/associativity:
= (5 ^ 5) ^ 3 ^ 7
# Step 2: Apply x ^ x = 0
= 0 ^ 3 ^ 7
# Step 3: x ^ 0 = x
= 3 ^ 7
# Step 4: compute
= 4

# Rearrangement saved work because duplicates cancel regardless of where they were.



'''
Q3. How can XOR *swap two numbers* without a temporary variable?
Ans:
Using XOR three times swaps values because XOR is reversible and uses no extra storage.
'''
# Let a = 9 (1001), b = 5 (0101)

# Step 1: a = a ^ b
a = 9 ^ 5 = 12   # (1001 ^ 0101 = 1100)

# Step 2: b = a ^ b    (now a is 12)
b = 12 ^ 5 = 9    # (1100 ^ 0101 = 1001) → original a

# Step 3: a = a ^ b    (now b is original a)
a = 12 ^ 9 = 5     # (1100 ^ 1001 = 0101) → original b

# Final: a = 5, b = 9  (values swapped)

# ==== CODE ====

# XOR Swap in Python

a = 9
b = 5

print("Before swap:")
print("a =", a, "b =", b)

# Step 1
a = a ^ b
# Step 2
b = a ^ b
# Step 3
a = a ^ b

print("\nAfter swap:")
print("a =", a, "b =", b)

# OUTPUT:
# Before swap:
# a = 9 b = 5

# After swap:
# a = 5 b = 9



'''
Q5. How does XOR detect *parity* (odd/even counts of 1-bits or odd occurrences)?
Ans:
XOR of bits yields 1 if an odd number of inputs have 1. 
When XORing a list of values, a nonzero result often indicates an odd-occurring element or odd parity.
'''
# Example A: parity of bits (single-bit view)
# inputs: 1, 1, 0, 1  (count of 1s = 3 → odd)
parity = 1 ^ 1 ^ 0 ^ 1 = 1   # result 1 → odd parity

# Example B: detect an element with odd occurrences
list = [2,3,2,4,3]   # 4 appears once (odd), others cancel
res = 0
res ^= 2   # 2
res ^= 3   # 2 ^ 3
res ^= 2   # (2 ^ 2) ^ 3 = 0 ^ 3 = 3
res ^= 4   # 3 ^ 4
res ^= 3   # (3 ^ 3) ^ 4 = 0 ^ 4 = 4
# result = 4 → the odd-occurrence element
