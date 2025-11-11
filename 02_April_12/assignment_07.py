'''
Problem 6 : Find max of 3 elements
'''
from typing import List
def find_maximum(numbers: List[int])->int:
    """
    Find the largest number in the provided list and return it.
    """
    if not numbers:
        raise ValueError("You have not provided even a single number.")
    return max(numbers)

def get_numbers(prompt: str)->List[int]:
    """
    Return a sequence of numbers after converting from one line input
    """
    while True: # this while true helped avoid tracebacks and we can try again here after invalid inputs
        try:
            user_input=input(prompt)
            return list(map(int, user_input.strip().split()))
        except ValueError:
            print("Please provide valid numbers")

numbers=get_numbers("Enter numbers in one line separated by single space: ")
print(find_maximum(numbers))
