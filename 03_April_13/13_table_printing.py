'''
Take input, print it's table.
'''

def table_print(number: int):
  """
  Table of the number from 1 to 10
  """
  for i in range(1,11):
    print(i*number)

def integer_input(prompt: str)->int:
  """
  Ensure valid integer input
  """
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print("Please enter a valid integer.")

number=integer_input("Enter an integer: ")
table_print(number)
