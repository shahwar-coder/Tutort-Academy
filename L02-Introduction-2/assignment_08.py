'''
Problem 7 : Find mid element out of 3 elements.
'''
from typing import List
def find_mid_element(numbers: List[int])->int:
  """
  Find the middle element and Return
  """
  if len(numbers) != 3:
      raise ValueError("Exactly 3 numbers are required.")
  return sorted(numbers)[1]
  
  
def get_input(prompt: str)->List[int]:
  """
  Ensure valid inputs before main logic procesing
  Return valid input for processing
  """
  while True:
    try:
      user_input=input(prompt)
      return list(map(int, user_input.strip().split()))
    except ValueError:
      print("Please enter valid integers.")

numbers=get_input("Enter numbers (integers): ")
print(find_mid_element(numbers))
