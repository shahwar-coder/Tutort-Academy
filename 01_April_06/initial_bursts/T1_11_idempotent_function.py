'''
- IDEMPOTENT FUNCTION
- A function is an idempotent function, if calling it once or multiple times makes no difference, or you can say has same effect.
- It's like saying : "do it once, or do it 100 times -- the result is the same."
- Real life Example: You lock the door by pressing the button. Now again if you keep presing you are going to find the door already locked, and eventually nothing changes.
'''

# Example : Idempotent Function
def make_even(n: int)->int:
    """Return even number, if not even ,make it even and return"""
    return n if n%2==0 else n+1

print(make_even(3))   # → 4
print(make_even(4))   # → 4
print(make_even(make_even(4)))  # → 4 

'''
- The result will be always an even number, no matter what is the input integer.
'''

# One Use in Software Engineering?
'''
API Example:

```
DELETE /users/5
```

- 1st call: deletes the user number 5
- 2nd call: no effect
- 3rd call: no effect
- 4th call: ......so on (no effect)
'''
