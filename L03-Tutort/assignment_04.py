'''
Write a program to display odd numbers till n
'''
def write_odds(number: int)->None:
    """
    Print all the odd numbers till number.
    """
    for i in range(1, number+1):
        if i%2==1:
            print(i)
            
def take_positive_integer(prompt: str)->int:
    """
    Ensure valid positive integer input
    """
    while True:
        try:
            number = int(input(prompt))
            if number<=0:
                print("Please enter a positive integer.")
            else:
                return number
        except ValueError:
            print("Enter a valid integer")

number=take_positive_integer("Enter a positive integer: ")
write_odds(number)
