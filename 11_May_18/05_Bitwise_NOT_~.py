'''
Q1. What does the bitwise NOT (~) operator do?
Ans:
The NOT operator flips every bit:
• 1 becomes 0  
• 0 becomes 1  
It inverts the entire binary pattern.
'''
# Example:
# ~1010 → 0101  (conceptually)



'''
Q2. Why does NOT behave differently in actual programming (like Python)?
Ans:
Because NOT (~) also applies two’s complement rules.
So ~n = -(n+1).
This happens because signed integers are stored in 2’s complement format.
'''
# Example 1
~5
= -(5 + 1)
= -6
# (~0101 = ...1010)

# Example 2
~0
= -(0 + 1)
= -1
# (~0000 = ...1111)

# Example 3
~1
= -(1 + 1)
= -2
# (~0001 = ...1110)

# Example 4
~(-1)
= -(-1 + 1)
= -0
= 0
# (~1111 = ...0000)

# Example 5
~10
= -(10 + 1)
= -11
# (~1010 = ...0101)

# Example 6
~(-5)
= -(-5 + 1)
= -(-4)
= 4
# (~...1011 = 0100)



'''
Q3. What is NOT used for in bitmasking?
Ans:
NOT is used to quickly create the **opposite mask**:
• turn all 1s→0s  
• turn all 0s→1s  
This helps when clearing or isolating bits.
'''
# Example:
# mask = 00101100
# ~mask flips all bits → 11010011



'''
Q4. How can NOT help clear a specific bit?
Ans:
To clear the k-th bit:
Use: n & ~(1 << k)
NOT flips the single-bit mask so that AND can turn that bit OFF.
'''
# Example:
# Clear bit 2:
# ~(0100) = 1011
# n & 1011 → clears bit 2



'''
Q5. What must you be careful about when using ~ in code?
Ans:
NOT always flips **all bits**, not just a few.
This can produce negative numbers due to two’s complement,
so you must apply masks when working with fixed sizes (like 32-bit, 16-bit).
'''
# Example:
# ~n & 0xFF ensures an 8-bit NOT operation.

