'''
Problem 1 : Find Minimum of three numbers (do not use min())
'''
from typing import Sequence #,Union
def find_minimum(numbers: Sequence[float|int])->float: # Sequence[Union[float,int]]
  """
  Find and return the minimum of exactly 3 numbers.
  Raises ValueError if input does not contain 3 elements.
  """
  if len(numbers)!=3:
    raise ValueError("Three numbers are required.")

  smallest=numbers[0]
  for n in numbers[1:]:
    if n < smallest:
      smallest=n
  return smallest

numbers=[3,2,9]
minimum_number=find_minimum(numbers)
print(minimum_number)
