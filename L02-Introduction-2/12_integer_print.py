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

            
