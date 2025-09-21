# First class function (function as an argument)
'''
2. Function as Argument
Task:
Write a function apply_to_list(func, items) that takes:

func: a function accepting a single argument,

items: a list of values,

and returns a new list where each element is func(item).

def square(x):
    return x * x

```
nums = [1, 2, 3]
print(apply_to_list(square, nums))  
# Expected output: [1, 4, 9]
```
'''
def square(x):
    return x**2

nums=[1,2,3]
def apply_to_list(func, nums):
    "Square everything in a list"
    return list(map(func, nums))

print(apply_to_list(square, nums))
