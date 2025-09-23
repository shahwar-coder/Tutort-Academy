'''
Problem 1 : Find Minimum of three numbers
'''
from typing import Sequence
def find_minimum(numbers: Sequence[float|int])->float:
  """
  Find and return the minimum of exactly 3 numbers.
  Raises ValueError if input does not contain 3 elements.
  """
  if len(numbers)!=3:
    raise ValueError("Three numbers are required.")
  return min(numbers)

numbers=[3,2,9]
minimum_number=find_minimum(numbers)
print(minimum_number)
