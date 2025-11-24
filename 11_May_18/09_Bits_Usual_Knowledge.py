'''
Q1. What special pattern does (2^k – 1) always have?
Ans:
One less than a power of 2 has all lower bits set to 1.
That means every bit below the leading 1 becomes 1.
'''
# Example:
# 7  →  0111   (8 - 1)
# 15 →  01111  (16 - 1)
# 31 →  011111 (32 - 1)



'''
Q2. What binary identity always holds for any k ≥ 1?
Ans:
2^k     = 1000…0  (one 1-bit at position k)
2^k – 1 = 0111…1  (all bits below position k become 1)
'''
# Example:
# 2^5 = 32 = 100000
# 31 =  11111 = (2^5 - 1)



'''
Q3. How does this help in checking if a number is a power of 2?
Ans:
If n is a power of 2:
n     = 1000…0  
n - 1 = 0111…1  
Their AND becomes 0.

So power-of-2 test:
(n & (n - 1)) == 0
'''
# Example:
# 8 & 7 = 1000 & 0111 = 0000 → power of 2



'''
Q4. Why is the identity (a | b) & a = a always true?
Ans:
OR never removes 1-bits from a.  
AND with a then keeps only a’s bits.  
So the final result must be exactly a.
'''
# Example:
# a = 1010, b = 1100
# a|b = 1110
# (a|b)&a = 1110 & 1010 = 1010 = a
