"""
Q. Take two inputs from the user and then ask the user if they want to add, subtract, multiply or divide.
Then based on user preference perform the operation.

Choices:
0: add
1: subtract
2: multiply
3: divide

Example 1:
Input: 2 4 3
Output: 0.5  # (2 / 4)

Example 2:
Input: 10 5 1
Output: 5  # (10 - 5)
"""
from typing import Iterator

def add(x,y):
  return x+y

def subtract(x,y):
  return x-y

def multiply(x,y):
  return x*y

def divide(x,y):
  if y==0:
    return "Cannot divide by zero"
  return x/y

operations_map={
  0: add,
  1: subtract,
  2: multiply,
  3: divide,
}

def get_x_y_choice(prompt: str)->Iterator[int]:
  """
  """
  

x,y,choice = map(int, input("Enter two numbers and a choice (0: add, 1: subtract, 2: multiply, 3: divide)").split())
result = operations_map.get(choice, lambda a,b: "Invalid choice")(x,y)
