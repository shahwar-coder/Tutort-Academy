'''
Q1. What is a function in Python?
Ans:
- A function is an independent block of reusable code.
- Defined with `def` and called directly by name.

Example:
'''
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))

# Step-by-step:
# 1. greet defined independently.
# 2. greet("Alice") executes → "Hello, Alice".



'''
Q2. What is a method in Python?
Ans:
- A method is a function that is bound to an object.
- Called with dot notation and often manipulates that object’s data.

Example:
'''
s = "Hello"
print(s.lower())

# Step-by-step:
# 1. "Hello" is a string object.
# 2. lower() is a method bound to that object.
# 3. Produces "hello".




'''
Q3. What’s the relationship between methods and functions?
Ans:
- Technically, methods are functions defined inside a class.
- They automatically take the instance (self) as their first argument.

Example:
'''
class Greeter:
    def say_hi(self, name):
        return f"Hi {name}"

g = Greeter()
print(g.say_hi("Bob"))

# Step-by-step:
# 1. say_hi is defined like a normal function.
# 2. When called via object g, Python passes g as self.
# 3. Returns "Hi Bob".




'''
Q4. Why do methods use dot notation?
Ans:
- Dot notation tells Python “call this function on this object.”
- The object is passed in automatically.

Example:
'''
lst = [3,1,2]
lst.sort()
print(lst)

# Step-by-step:
# 1. lst is a list object.
# 2. lst.sort() is method → sorts in-place.
# 3. Output: [1,2,3].


'''
Q5. Can a function become a method?
Ans:
- Yes, when defined inside a class, it becomes a method.
- Same code, but different context.

Example:
'''
def add(a,b): return a+b  # normal function

class Math:
    def add(self,a,b): return a+b  # method

print(add(2,3))           # 5
print(Math().add(2,3))    # 5

# Step-by-step:
# Both do the same, but one is standalone, one is tied to an object.




'''
Q6. Quick shorthand
- Function = standalone tool.
- Method = function bound to object (dot notation).
- All methods are functions, not all functions are methods.
'''
