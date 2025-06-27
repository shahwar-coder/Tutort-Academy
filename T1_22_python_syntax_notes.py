'''
1. Indentation is mandatory:
'''
if True:
    print("Hello")

'''
2. Colons after blocks:
'''
x=5
if x > 0:
    print("Positive")

'''
3. Variables must be assigned before use.
'''
a = 5    
print(a)


'''
4. Case Sensitivity matters
'''
name = "Alice"
Name = "Bob"

print(name)  # Alice
print(Name)  # Bob

'''
5. Correct function declaration
- def
- proper name
- colon
- indented block of code
'''
def greet(name):
    print("Hello", name)


'''
6. Careful String Quotes
'''
x = "hello"   
y = 'world'    
z = "don't"   

'''
7. Importing modules
- Do not ever import under loops, or frequently used functions
'''
import math
from math import sqrt


'''
8. Avoid Trailing Commas or Semi Colons
'''
print("Hello",) # still valid but unnecessary
print("Hello"); # Works but not recommended


'''
9. Do not use true, false, null
- Instead : Use True, False, None — Capitalized
'''

'''
10. Do not use reserved keywords as variables.
11. Use 'is' for identity and '==' for equality
'''
a = [1, 2]
b = [1, 2]

print(a == b)  # ✅ True (same values)
print(a is b)  # ❌ False (different objects)


