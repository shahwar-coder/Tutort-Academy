'''
Problem 5 : Check number is odd or not, print odd or even.
'''
def odd_check(number: int)->bool:
  """
  Return True if number is odd, False otheriwise
  """
  return number%2!=0
  
def get_user_number(prompt: str)->int:
  """
  Ensure valid input and then return it.
  """
  while True: #give robustness (until a valid input comes in from user we keep asking for it)
    try:
      return int(input(prompt))
    except ValueError:
      print("Please input a valid integer.")

number=get_user_number("Enter an integer: ")
print("Odd" if odd_check(number) else "Even")

