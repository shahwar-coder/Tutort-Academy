'''
Q. Problem 2 : Check couple is eligible for marriage (girl age should be 18 boy
should be 21) print yes or no
'''

def marriage_eligibility(boy_age: int, girl_age: int)->bool:
  """
  Return True if marriage is possible, otherwise False
  """
  if not isinstance(boy_age, int) or not isinstance(girl_age, int):
    raise ValueError("Age should be an Integer.")
  return boy_age>=21 and girl_age>=18

def get_int_input(prompt: str)->int:
  """
  In case user inputs a value that cannot be type casted to int (we need to handle that before entering to main logic)
  """
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print("Invalid Input, Please enter a valid interger")
  
boy_age = get_int_input("Enter boy's age: ")
girl_age = get_int_input("Enter girl's age: ")

if marriage_eligibility(boy_age, girl_age):
  print("Yes")
else:
  print("No")
