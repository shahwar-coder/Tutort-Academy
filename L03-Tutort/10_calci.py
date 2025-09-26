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

def get_x_y_choice(prompt: str)->tuple[int,int,int]:
  """
  Ensure valid inputs
  """
  while True:
    try:
      user_input=tuple(list(map(int, input(prompt).split())))
      if len(user_input)!=3:
        print("Please enter exactly 2 numbers and 1 choice.")
        continue
      return user_input
    except ValueError:
      print("Please enter valid inputs.")
  

x,y,choice = get_x_y_choice("Enter two numbers and a choice (0: add, 1: subtract, 2: multiply, 3: divide)")
result = operations_map.get(choice, lambda a,b: "Invalid choice")(x,y)
print(result)
