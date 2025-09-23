'''
Problem 3 : Print tax amount if bill amount is 50000 above then tax is 10%
else 5% , using ternary operator.
'''
# I will use conditional expression, as Python does not have Ternary operator.

import math
def calculate_tax(bill_amount: float) -> float:
    """
    Return the tax on the bill amount.
      - 10% if bill is above 50000
      - 5% otherwise
    """
    return 0.1 * bill_amount if bill_amount > 50000 else 0.05 * bill_amount

def get_bill(prompt: str) -> float:
    """
    Prompt user for a valid bill amount.
    Ensures the input is a finite float number.
    Keeps asking until a valid number is provided.
    """
    while True:
        try:
            user_input = float(input(prompt))
            if math.isfinite(user_input):
                return user_input
            else:
                print("Bill should be a finite float number.")
        except ValueError:
            print("Please enter a valid floating number.")

bill_amount = get_bill("Enter Bill Amount: ")
tax_calculated = calculate_tax(bill_amount)
print(f"Total Tax: {tax_calculated}")
