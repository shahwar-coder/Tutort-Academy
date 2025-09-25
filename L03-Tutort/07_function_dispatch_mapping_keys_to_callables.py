def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a // b if b != 0 else "Div by 0"

ops = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

def calc(op, x, y):
    func = ops.get(op)
    if func is None:
        return "Unknown operation"
    return func(x, y)

print(calc("+", 10, 3))  # 13
print(calc("/", 10, 0))  # Div by 0

'''
Key points:
- Store functions as values, look them up, then call.
- Keeps the "what to do" separate from the "when to do it."
- Good for small command systems, REPLs, simple routers.
'''
