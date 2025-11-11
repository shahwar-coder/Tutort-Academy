'''
Q1. What does "inf" mean in Python floats?
Ans:
- It represents positive infinity (larger than any number).
- Comes from overflow or explicit float("inf").

Example:
'''
import math
x = float("inf")
print(x, math.isinf(x))

# Step-by-step:
# 1. float("inf") creates infinity.
# 2. math.isinf(x) → True.



'''
Q2. What about negative infinity?
Ans:
- float("-inf") represents negative infinity.
- Smaller than any finite number.

Example:
'''
y = float("-inf")
print(y < -1e308)

# Step-by-step:
# -inf is less than any large negative number → True.



'''
Q3. What does "nan" mean and when does it occur?
Ans:
- "Not a Number" → result of undefined operations (like inf - inf).
- Any comparison with nan is False (even nan == nan).

Example:
'''
z = float("nan")
print(z == z, math.isnan(z))

# Step-by-step:
# 1. nan == nan → False.
# 2. math.isnan(z) → True (only reliable way to check).



'''
Q4. Why doesn’t 1.0/0.0 give inf in Python?
Ans:
- Python raises ZeroDivisionError instead of producing inf.
- Explicit floats like float("inf") must be used to represent infinity.

Example:
'''
try:
    print(1.0 / 0.0)
except ZeroDivisionError as e:
    print("Error:", e)

# Step-by-step:
# Division by 0 → ZeroDivisionError raised, not inf.



'''
Q5. How do nan/inf differ from normal exceptions?
Ans:
- They are valid float values, not errors.
- You must detect them with math.isnan() or math.isinf().
'''



'''
Q6. How to handle nan/inf in computations safely?
Ans:
- Use math.isinf() and math.isnan() to detect.
- Replace or ignore them in calculations.

Example:
'''
nums = [1.0, float("inf"), float("nan"), 5.0]
cleaned = [x for x in nums if not (math.isinf(x) or math.isnan(x))]
print(cleaned)

# Step-by-step:
# Filters out inf and nan.
# Keeps [1.0, 5.0].



'''
Q7. Quick shorthand
- inf → positive infinity.
- -inf → negative infinity.
- nan → not a number (never equal to itself).
- Detection: math.isinf(), math.isnan().
- Division by zero raises error (not inf/nan).
'''



'''
Q8: What does math.isfinite(x) do?
Ans:
- Returns True if x is neither infinity nor NaN.
- Basically: finite real numbers only.

Example:
'''
import math

print(math.isfinite(3.14))          # True
print(math.isfinite(float("inf")))  # False
print(math.isfinite(float("nan")))  # False

# Step-by-step:
# 1. 3.14 → finite → True.
# 2. inf → not finite → False.
# 3. nan → not finite → False.

