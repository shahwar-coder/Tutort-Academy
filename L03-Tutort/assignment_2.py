'''
Problem 2 : Write a program that prompts the user to input an integer
and then outputs the number with the digits reversed. For example, if the
input is 12345, the output should be 54321
'''

def reverse_digits(digits: int)->int:
  """
  Reverse and then return the reversed digits
  """
  return int("".join(reversed(list(str(digits)))))
      
  
def get_integer(prompt: str)->int:
  """
  Ensure valid integer input
  """
  try:
    return int(input(prompt))
  except ValueError:
    print("Please enter a valid integer.")

digits=get_integer("Enter an integer: ")
print(reverse_digits(digits))
