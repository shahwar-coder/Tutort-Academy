'''
Take integer input, if odd -> print all odd till 10, and if even -> print all even till 10
'''

def odd_even_result(number: int):
  """
  Print all odd till 10 if input number is odd
  Print all even till 10 if input number is even
  """
  if number%2!=0:
    for n in range(1,11,2):
      print(n)
  else:
    for n in range(0,11,2):
      print(n)
      

def integer_input(prompt: str)->int:
  """
  Ensure valid integer input
  """
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print("Please enter valid integer")

number=integer_input("Enter an integer")
odd_even_result(number)
