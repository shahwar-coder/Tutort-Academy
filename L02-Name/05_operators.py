'''
Q1. What are arithmetic operators in Python?
Ans:
- Perform basic math: +, -, *, /, %, ** (power), // (floor division).

Example:
'''
a, b = 7, 3
print(a + b, a / b, a // b, a ** b)

# Step-by-step:
# 1. 7+3 = 10
# 2. 7/3 = 2.333...
# 3. 7//3 = 2 (floor division)
# 4. 7**3 = 343



'''
Q2. How do comparison operators work?
Ans:
- Compare two values, returning True/False.
- Can be chained (1 < x < 5).

Example:
'''
x = 4
print(x > 2, x == 4, 1 < x < 5)

# Step-by-step:
# 1. x>2 → True
# 2. x==4 → True
# 3. 1<x<5 → True (chained comparison).



'''
Q3. What are logical operators?
Ans:
- Combine conditions: and, or, not.
- They short-circuit (stop evaluating when result is known).

Example:
'''
x = 0
print(x and 5, x or 5, not x)

# Step-by-step:
# 1. x=0 → falsy → x and 5 = 0 (stops early).
# 2. x or 5 = 5 (since x falsy, return 5).
# 3. not x → True (since 0 is falsy).



'''
Q4. What are assignment & augmented assignment operators?
Ans:
- = assigns, += etc. update in-place if possible.
- For mutables → modifies object, for immutables → new object.

Example:
'''
x = 5
x += 2
print(x)

lst = [1,2]
lst += [3]
print(lst)

# Step-by-step:
# 1. x=5 → int (immutable). x+=2 creates new int → 7.
# 2. list [1,2] (mutable). += appends → [1,2,3].



'''
Q5. What are bitwise operators?
Ans:
- Work on binary form: &, |, ^, ~, <<, >>.
- Often used in low-level tasks.

Example:
'''
a, b = 6, 3   # 6=110, 3=011
print(a & b, a | b, a ^ b, a << 1, a >> 1)

# Step-by-step:
# 1. 110 & 011 = 010 = 2
# 2. 110 | 011 = 111 = 7
# 3. 110 ^ 011 = 101 = 5
# 4. 110 << 1 = 1100 = 12
# 5. 110 >> 1 = 011 = 3



'''
Q6. What are membership operators?
Ans:
- in / not in → check presence in sequence.

Example:
'''
nums = [1,2,3]
print(2 in nums, 4 not in nums)

# Step-by-step:
# 1. 2 in nums → True
# 2. 4 not in nums → True



'''
Q7. What are identity operators?
Ans:
- is / is not check if two names point to the SAME object (not just equal value).

Example:
'''

a = [1,2]
b = [1,2]
print(a == b, a is b)

# Step-by-step:
# 1. a==b → True (values equal).
# 2. a is b → False (different objects in memory).



'''
Q8. What is operator precedence and why does it matter?
Ans:
- Determines evaluation order.
- Parentheses () override.

Example:
'''
print(2 + 3 * 4, (2 + 3) * 4)

# Step-by-step:
# 1. 3*4=12 → 2+12=14
# 2. Parentheses: (2+3)=5 → 5*4=20
