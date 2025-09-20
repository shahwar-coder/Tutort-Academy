'''
- duck typing?
- duck typing is a type of system where behaviour of the object is more of a concern than the actual type of the object.
- it comes from the saying "if it looks like a duck, swims like a duck and quacks like a duck then probably it is a duck"

- Python is a dynamically typed language
- we do not need to declare the type of variables (objects)
'''

# Example (NOT DUCK TYPING)
def add_numbers(a, b):
    return a + b

print(add_numbers(10, 5))      # 15
print(add_numbers(3.5, 2.5))   # 6.0


# Example (FULL DUCK TYPING)
class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm pretending to be a duck!")

def make_it_quack(thing):
    thing.quack()  # We don't care what type 'thing' is!

d = Duck()
p = Person()

make_it_quack(d)  # ✅ Works
make_it_quack(p)  # ✅ Also works!


# Important Notes:
'''
- Both are showing dynamic behaviour
- Only second one is classic duck typing example, because it assumes a behaviour without checking the type, a pure custom behaviour is defined.
    - We don’t care if it’s a Duck class, Person, or Robot, as long as it quacks
- First one, is not duck typing because:
    - it relies on built-in operator, not custom behaviour/method
    - and to the extent no behaviour is assumed at all in the first case
    - it's dynamic typing not duck typing
'''
