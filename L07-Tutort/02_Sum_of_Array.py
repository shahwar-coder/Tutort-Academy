'''
Sum of integers of Array/List
'''
from typing import List
arr = [1,2,3,4,5,6]

def add_array_elements(arr: List[int])->int:
  """
  Add integers of an array
  """
  return sum(arr)

print(add_array_elements(arr))
