'''
Q1. How does Python define code blocks?
Ans:
- Python uses **indentation** (spaces/tabs), not braces `{}` like C/Java.
- Consistent indentation is required; mixing tabs/spaces causes errors.
'''
# Example (correct):
if True:
    print("Indented block")

# Example (error):
if True:
print("Not indented")   # ❌ IndentationError

# Step-by-step:
# 1. Python sees no indentation → can’t tell block scope.
# 2. Raises IndentationError.



'''
Q2. Is Python case-sensitive?
Ans:
- Yes, identifiers are case-sensitive.
- `myVar` ≠ `myvar`.

Example:
'''
x = 5
print(x)      # 5
print(X)      # ❌ NameError: X not defined




'''
Q3. Why do we need colons (:) in Python?
Ans:
- Colon marks the start of a new block (`if`, `for`, `while`, `def`, `class`).

Example:
'''
def greet():
    print("Hello")

# Step-by-step:
# 1. def greet() defines a function.
# 2. Colon tells Python: "next indented lines = function body".



'''
Q4. How are comments written in Python?
Ans:
- Use `#` for single-line comments.
- Everything after `#` is ignored by interpreter.

Example:
'''
# This is a comment
x = 10  # inline comment
print(x)   # prints 10



'''
Q5. What does dynamic typing mean in Python?
Ans:
- No need to declare variable type; type is determined at runtime.
- Same variable can hold different types during execution.

Example:
'''
a = 10       # int
a = "hello"  # now str
print(a)

# Step-by-step:
# 1. a bound to int → 10.
# 2. Reassigned to str → "hello".
# 3. Dynamic typing lets this happen without error.



'''
Q6. (Extra) What about line continuation and reserved keywords?
Ans:
- Python normally ends a statement at line break.
- Use "\" for explicit continuation or () [] {} for implicit continuation.
- Reserved keywords (if, for, class, etc.) cannot be used as variable names.

Example:
'''
# Line continuation
total = (1 +
         2 +
         3)
print(total)

# Step-by-step:
# 1. Parentheses allow implicit continuation.
# 2. Adds up to 6.

# Keyword error
# class = 5   # ❌ SyntaxError, 'class' is reserved
