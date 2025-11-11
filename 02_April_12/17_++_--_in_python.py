'''
Q1. Does Python support ++ or -- operators?
Ans:
- No, Python does not have ++ or --.
- Instead, use +=1 or -=1.

Example:
'''
x = 5
x += 1   # increment
print(x) # 6
x -= 1   # decrement
print(x) # 5



'''
Q2. Why doesn’t Python have ++ or --?
Ans:
- For clarity and simplicity.
- ++/-- can be confusing in other languages (pre/post increment).
- Python wants explicit, readable operations.
'''



'''
Q3. How does immutability of integers relate here?
Ans:
- Integers are immutable.
- x += 1 creates a new int object and rebinds x to it.
- Not an in-place change.

Example:
'''
x = 10
print(id(x))
x += 1
print(id(x))

# Step-by-step:
# IDs differ → shows new object created, not mutation.



'''
Q4. What alternatives exist beyond += / -=?
Ans:
- range() handles increments in loops.
- operator module for arithmetic operations.
- Custom inc/dec functions.

Example:
'''
import operator
x = 7
x = operator.add(x, 1)   # increment
print(x)                 # 8



'''
Q5. Quick shorthand
- No ++ / -- in Python.
- Use +=1 / -=1.
- Integers immutable → rebinding, not mutation.
- Python favors explicit, readable style.
'''
