'''
Q1. What are Python’s numeric types?
Ans:
- int (whole numbers), float (decimals), complex (real + imaginary).
Example:
'''
a = 10        # int
b = 3.14      # float
c = 2 + 3j    # complex
print(type(a), type(b), type(c))

# Step-by-step:
# a is int, b is float, c is complex.



'''
Q2. What are sequence types in Python?
Ans:
- str (immutable text), list (mutable), tuple (immutable sequence).
Example:
'''
s = "hello"
lst = [1, 2, 3]
t = (4, 5, 6)
lst.append(4)   # works (mutable)
# s[0] = "H"   # ❌ error (str immutable)



'''
Q3. What’s the difference between set and frozenset?
Ans:
- set → unordered, mutable, unique elements.
- frozenset → immutable set.
Example:
'''
s = {1, 2, 2, 3}
fs = frozenset([1, 2, 3])
print(s, fs)

# Step-by-step:
# s keeps only unique elements → {1, 2, 3}
# fs is frozen → can’t add/remove.



'''
Q4. What is a mapping type in Python?
Ans:
- dict: key-value pairs, keys must be hashable.
Example:
'''
person = {"name": "Alice", "age": 30}
print(person["name"])

# Step-by-step:
# dict maps "name" → "Alice", "age" → 30.




'''
Q5. How do booleans behave in Python?
Ans:
- bool has only True and False.
- But many values evaluate as True/False in conditions.
Example:
'''
print(bool(0), bool(42), bool(""), bool("hi"))

# Step-by-step:
# 0 and "" are False → False
# 42 and "hi" are True → True



'''
Q7. How does type casting work?
Ans:
- Use built-in functions: int(), float(), str(), list(), tuple(), set().
Example:
'''
x = "123"
print(int(x), float(x), list(x))

# Step-by-step:
# "123" → 123 (int), 123.0 (float), ['1','2','3'] (list of chars).
