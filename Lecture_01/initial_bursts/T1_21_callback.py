'''
1. CALLBACK
- a function
- it is passed as an argument to another function, and is expected to be called back (obviously for execution)
- It's like saying : "Hey, when you are done, execute this function!!"
'''

# Example:

def greet(name):
    print(f"Hi {name}")

def do_something(callback):
    print(f"I am trying to do something")
    callback("Shahwar")

do_something(greet)

# OUTPUT:
'''
I am trying to do something
Hi Shahwar
'''

# FLOW:
'''
1. You pass `greet` function into `do_something` as `callback`.
2. `do_something` does something, then calls `callback("Alice")`.
3. That runs `greet("Shahwar")`.
'''
