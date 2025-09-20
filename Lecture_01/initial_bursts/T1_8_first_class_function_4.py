'''
3. Function Factory
Task:
Write a function make_multiplier(n) that returns a new function. The returned function should take one argument x and return x * n.

Example use:

```
double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # Expected: 10
print(triple(5))  # Expected: 15
```
'''

def make_multiplier(n):
    def multiply(x):
        return x*n
    return multiply

double=make_multiplier(2) # double has a function stored now, which is multiply, now again a parameter for x needs to be passed AND internally it will look like : <function make_multiplier.<locals>.multiply at 0x10222f600>
print(double(10))

triple=make_multiplier(3)
print(triple(10))

quad=make_multiplier(4)
print(quad(10))

quin=make_multiplier(5)
print(quin(10))

'''
Output:
20
30
40
50
'''
