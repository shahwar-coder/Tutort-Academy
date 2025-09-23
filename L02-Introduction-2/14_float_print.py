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
            print("Invalid, Although nan or inf are acceptable float, please entwr finite float.")
        except ValueError:
          print("Invalid Input! Enter Finite Float.")

point_number=get_user_input()
print(f"Your Float is: {point_number}")

            
