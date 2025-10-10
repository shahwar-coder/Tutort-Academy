'''
Problem 1 : Write a program to calculate the sum of the first 10 natural
numbers.
'''
def sum_calculation():
  """
  Calculate sum of 10 natural numbers
  """
  return sum(range(1,11))

print(sum_calculation())


# OR ==============================
# OR ============================== Speed : ✅ [MATHEMATICAL FORMULA APPROACH] -> O(1) — constant time
# OR ============================== Speed : ❌ [SUM FUNCTION APPROACH] -> O(n), loops from 1 to n
# OR ==============================


def sum_calculation(n: int)->int:
  """
  Calculate sum of 10 natural numbers
  """
  return n*(n+1)//2

print(sum_calculation(n=10))
