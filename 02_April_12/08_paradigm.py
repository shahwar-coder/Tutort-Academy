'''
Q1. What is a programming paradigm?
Ans:
- A paradigm is a style or philosophy of writing code.
- It dictates how problems are structured and solved.

Example:
'''
# Same problem: sum of numbers
# Different paradigms give different approaches.



'''
Q2. What is the procedural paradigm?
Ans:
- Focuses on step-by-step instructions and functions.
- Code organized into procedures.

Example:
'''
def add_numbers(nums):
    total = 0
    for n in nums:
        total += n
    return total

print(add_numbers([1,2,3]))  # 6

# Step-by-step:
# 1. Function describes explicit procedure.
# 2. Uses loop + accumulator variable.



'''
Q3. What is the object-oriented paradigm?
Ans:
- Organizes code into classes and objects.
- Encapsulation: data + behavior together.

Example:
'''
class Calculator:
    def __init__(self):
        self.total = 0
    def add(self, n):
        self.total += n

c = Calculator()
c.add(5)
c.add(10)
print(c.total)  # 15

# Step-by-step:
# 1. Calculator object stores state.
# 2. add() method updates that state.



'''
Q4. What is the functional paradigm?
Ans:
- Focuses on pure functions (no side effects) and immutability.
- Often uses map, filter, reduce.

Example:
'''
nums = [1,2,3,4]
squares = list(map(lambda x: x*x, nums))
print(squares)

# Step-by-step:
# 1. map applies lambda to each number.
# 2. Returns [1,4,9,16].



'''
Q5. What is the declarative paradigm?
Ans:
- Focuses on *what* should be done, not *how*.
- Common in SQL, config, and some Python patterns.

Example:
'''
nums = [1,2,3,4,5]
evens = [n for n in nums if n % 2 == 0]
print(evens)

# Step-by-step:
# 1. List comprehension “declares” intent: pick even numbers.
# 2. Python handles iteration behind the scenes.



'''
Q6. What makes Python multi-paradigm?
Ans:
- Python lets you mix paradigms freely:
   - Write procedural scripts.
   - Build OOP systems.
   - Use functional tools like map, filter, reduce.
- Flexibility is one of Python’s strengths.
'''



'''
Q7. Quick shorthand
- Procedural → step-by-step functions.
- OOP → classes, objects, state.
- Functional → pure functions, immutability.
- Declarative → what, not how.
- Python = supports multiple.
'''
