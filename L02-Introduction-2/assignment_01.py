'''
Problem 1 : Find Minimum of three numbers
'''
from typing import Sequence #,Union
def find_minimum(numbers: Sequence[float|int])->float: #or Sequence[Union[float, int]
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



'''
Summary: Find Minimum of Exactly 3 Numbers (using min)

Approach:
- Function expects exactly 3 numbers (int or float).
- Validate input length; raise ValueError if not 3 elements.
- Use built-in min() to compute and return the smallest value.

Key Points:
- Strictly enforces 3-element input.
- Clear error handling for invalid input length.
- Concise and efficient: O(1) for length check + O(n) for min().
'''
