'''
Q. Take an float from user and print it.
'''
import math
def get_user_input()->float:
    """
    Take user input as a float and return it.
    Enter 'q' or 'quit' to exit the program.
    Raises SystemExit when quitting.
    """
    while True:
        user_input=input("Enter Float (or q/quit to quit): ")
        if user_input.lower() in ['q', 'quit']:
            raise SystemExit("User quit the program!")
        try:
          number=float(user_input)
          if math.isfinite(number):
            return number
          else:
            print("Invalid, Although nan or inf are acceptable float, please enter finite float.")
        except ValueError:
          print("Invalid Input! Enter Finite Float.")

point_number=get_user_input()
print(f"Your Float is: {point_number}")



'''
Summary: Float Input with Validation and Quit Option

Approach:
- Function get_user_input() -> float loops until valid input is given.
- Accepts user input and strips/normalizes it.
- If user types 'q' or 'quit', raise SystemExit to exit.
- Try converting input to float.
- Use math.isfinite() to reject nan, inf, -inf; show message and retry.
- If conversion fails (ValueError), show error message and retry.
- Return valid finite float once provided.

Key Points:
- Handles invalid input gracefully with retry.
- Ensures returned value is a valid finite float.
- Provides clean quit option for user.
'''

            
