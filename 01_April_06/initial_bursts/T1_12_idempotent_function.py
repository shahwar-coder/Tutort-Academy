'''
🧠 Question: Create an Idempotent Function
Write a function called set_to_zero_if_negative(n) that:

Takes an integer n as input

If n is negative, returns 0

If n is non-negative, returns it unchanged

Then prove that your function is idempotent by calling it multiple times on the same input and printing the results.

✅ Example:

```
print(set_to_zero_if_negative(-5))               # Output: 0
print(set_to_zero_if_negative(7))                # Output: 7
print(set_to_zero_if_negative(set_to_zero_if_negative(-5)))  # Output: 0
```
'''

def set_to_zero_if_negative(n: int)->int:
    "Set to zero if integer is negative"
    return 0 if n<0 else n

print(set_to_zero_if_negative(-5))               # Output: 0
print(set_to_zero_if_negative(7))                # Output: 7
print(set_to_zero_if_negative(set_to_zero_if_negative(-5)))  # Output: 0
# Proving idempotency: calling function again doesn’t change result
