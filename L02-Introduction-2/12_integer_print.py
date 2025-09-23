'''
Q. Take an integer from user and print it.
'''
def get_user_input()->int:
    """
    Take user input (integer) and return
    Raise SystemExit for quitting
    """
    while True:
        user_input=input("Enter Integer: ")
        if user_input.lower() in ['q', 'quit']:
            raise SystemExit("User quit the program!")
        try:
            return int(user_input)
        except ValueError:
            print("Invalid Input!")

number=get_user_input()
print(f"your Integer is: {number}")



'''
Summary: Integer Input with Validation and Quit Option

Approach:
- Wrap input logic in a function get_user_input() -> int.
- Loop until valid input is provided.
- If user types 'q' or 'quit', raise SystemExit to exit program.
- Try converting input to int; if ValueError, show error message and retry.
- Return the valid integer once entered.

Key Points:
- Ensures only valid integers are accepted.
- Provides a clean quit option for user.
- Robust against invalid input, does not crash.
'''


            
