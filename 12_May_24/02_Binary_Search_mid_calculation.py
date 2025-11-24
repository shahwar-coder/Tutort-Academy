'''
Q1. Why do we have two formulas for finding mid in binary search?
Ans:
Because the usual formula (lo + hi) // 2 can overflow
in languages with fixed integer sizes.
The safer version avoids adding two large numbers.
'''
# Example:
# In C++: lo=2e9, hi=2e9 → lo+hi causes overflow.



'''
Q2. What is the unsafe mid formula?
Ans:
mid = (lo + hi) // 2
It works only when lo + hi is within the allowed integer range.
'''
# Example:
# Small numbers → OK: (10 + 18)//2 = 14



'''
Q3. What is the safe mid formula?
Ans:
mid = lo + (hi - lo) // 2
This avoids overflow by subtracting first, not adding two big values.
'''
# Example:
# 10 + (18-10)//2 = 10 + 4 = 14



'''
Q4. Do both formulas always give the same mid value?
Ans:
Yes, for small numbers.
Overflow happens only when lo + hi becomes too large
for the language’s integer limits.
'''
# Example:
# lo=10, hi=18 → both give 14.
# ...
# Unsafe:
# mid = (lo + hi) // 2
# mid = (10 + 18) // 2
# mid = 28 // 2
# mid = 14
# ...
# Safe:
# mid = lo + (hi - lo) // 2
# mid = 10 + (18 - 10) // 2
# mid = 10 + 8 // 2
# mid = 10 + 4
# mid = 14





'''
Q5. Why does Python never overflow with the unsafe formula?
Ans:
Python integers are unlimited in size.
So Python can compute lo + hi safely even for very large values.
'''
# Example:
# Python can store integers with hundreds of digits.



'''
Q6. In which languages is the safe formula essential?
Ans:
Languages with fixed-width integers like C, C++, Java.
They can overflow when lo and hi are large.
'''
# Example:
# In C++: int range is about ±2 billion → adding two large ints can overflow.

