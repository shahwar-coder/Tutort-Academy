'''
Write funcs for each calci func : add, sub, mul, div
Use them to solve an expression
'''

def add(a,b):
    """add two numbers"""
    return a+b

def subtract(a,b):
    """subtract two numbers"""
    return a-b

def multiply(a,b):
    """multiply two numbers"""
    return a*b

def divide(a,b):
    """divide two numbers"""
    if b==0:
        raise ValueError("Denominator cannot be zero.")
    return a/b

operations_map = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

a=5
b=7
operation="+"

function = operations_map.get(operation, None)
if function is None:
    print("Invalid operation requested")
else:
    result = function(a,b)
    print(result)
