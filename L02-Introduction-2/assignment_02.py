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



'''
Summary: Find Minimum Without Using min()

Approach:
- Assume the first element is the smallest.
- Loop through the rest of the numbers.
- If any number is smaller than the current smallest, update it.
- After the loop ends, return the smallest value.

Key Points:
- Works for int and float sequences of any length.
- Raises ValueError if sequence is empty.
- Time complexity: O(n), same as built-in min().
'''
