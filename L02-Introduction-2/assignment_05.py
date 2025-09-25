'''
Problem 4 : Check if the year is leap or not.

A year is a leap year if:
-> It can be divided by 400,
-> OR
-> It is NOT divisible by 100 and Divisible by 4
then it is a leap year.
'''
def is_leap_year(year: int)->bool:
  """
  Return True if the year is a leap year, otherwise False.
  """
  return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)

def get_year_input(prompt: str)->int:
  """
  Takes valid year input
  """
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print("Enter a valid integer.")

year=get_year_input("Enter year: ")
print("Leap Year" if is_leap_year(year) else "Not a Leap year")
