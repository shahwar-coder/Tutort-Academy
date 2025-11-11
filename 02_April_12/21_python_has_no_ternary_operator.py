'''
Q1. Does Python have a ternary operator like C/Java?
Ans:
- No traditional `?:`.
- Instead, Python uses a conditional expression:
  value_if_true if condition else value_if_false
'''
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)

# Step-by-step:
# 1. Condition age>=18 → True.
# 2. status = "Adult".



'''
Q2. How does Python’s syntax improve readability?
Ans:
- Reads like English: “Adult if age>=18 else Minor.”
- Easier to understand than ?: for beginners.
'''
x = 5
msg = "Positive" if x > 0 else "Non-positive"
print(msg)
# Step-by-step:
# x > 0 → True → "Positive".



'''
Q3. Can ternary expressions be nested?
Ans:
- Yes, but readability decreases.
- Better to use normal if-else for complex logic.
'''



'''
Q4. Where are ternary expressions commonly used?
Ans:
- Assignments, return values, and comprehensions.
'''
nums = [1, -2, 3]
labels = ["pos" if n > 0 else "neg" for n in nums]
print(labels)

# Step-by-step:
# For each n: if positive → "pos", else "neg".
# Output: ["pos","neg","pos"].



'''
Q5. How does ternary differ from normal if-else statements?
Ans:
- Ternary is an expression (returns value).
- if-else statement just controls flow.
'''
x = 7
# Statement version
if x%2==0:
    result = "Even"
else:
    result = "Odd"

# Ternary expression version
result2 = "Even" if x%2==0 else "Odd"

print(result, result2)



'''
Q6. Quick shorthand
- No ?: in Python.
- Use: A if condition else B.
- Concise but avoid over-nesting.
'''
