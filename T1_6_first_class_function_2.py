# ==> First Class Function (Assign function to a variable)
'''
1. Function Alias
Task:
Given this function:
```
def greet(name: str) -> str:
    return f"Hello, {name}!"
```
Example task to do: (or use any variable of your liking)
Assign greet to a new variable say_hello.
Call say_hello("Alice") and print the result.
'''

def greet(name: str)->str:
    "To greet"
    return f"Hello, {name}"

person=greet

print(person("Shahwar"))
