'''
Print if number is 10 , >10 or <10.
'''
def compare_with_ten(number: int)->str:
  """
  Return either number is equal to 10, >10, <10
  """
  if number==10:
    return "Number is Equal to 10"
  elif number<10:
    return "Number is < 10"
  else:
    return "Number is > 10"

def get_number(prompt: str)->int:
  """
  Ensure valid integer input before processing.
  """
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print("Please enter valid integer.")

number=get_number("Enter your integer: ")
print(compare_with_ten(number))
